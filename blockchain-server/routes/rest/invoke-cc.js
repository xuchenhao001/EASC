'use strict';

let express = require('express');
let router = express.Router();

let log4js = require('log4js');
let logger = log4js.getLogger('REST');
logger.level = 'DEBUG';

const FabricCAServices = require('fabric-ca-client');
const { Gateway, Wallets } = require('fabric-network');
const fs = require('fs');
const path = require('path');

let common = require('./common');

const networkScale = 'network-2-peers'

let enrollAdmin = async function() {
  logger.debug("Enroll admin...");
  try {
    // load the network configuration
    const ccpPath = path.resolve(__dirname, '..', '..', '..', 'fabric-samples', networkScale, 'organizations', 'peerOrganizations', 'org1.example.com', 'connection-org1.json');
    const fileExists = fs.existsSync(ccpPath);
    if (!fileExists) {
      throw new Error(`no such file or directory: ${ccpPath}`);
    }
    const ccp = JSON.parse(fs.readFileSync(ccpPath, 'utf8'));

    // Create a new CA client for interacting with the CA.
    const caInfo = ccp.certificateAuthorities['ca.org1.example.com'];
    const caTLSCACerts = caInfo.tlsCACerts.pem;
    const ca = new FabricCAServices(caInfo.url, { trustedRoots: caTLSCACerts, verify: false }, caInfo.caName);

    // Create a new file system based wallet for managing identities.
    const walletPath = path.join(__dirname, 'wallet');
    const wallet = await Wallets.newFileSystemWallet(walletPath);
    logger.info(`Wallet path: ${walletPath}`);

    // Check to see if we've already enrolled the admin user.
    const identity = await wallet.get('admin');
    if (identity) {
      logger.info('An identity for the admin user "admin" already exists in the wallet');
      return;
    }

    // Enroll the admin user, and import the new identity into the wallet.
    const enrollment = await ca.enroll({ enrollmentID: 'admin', enrollmentSecret: 'adminpw' });
    const x509Identity = {
      credentials: {
        certificate: enrollment.certificate,
        privateKey: enrollment.key.toBytes(),
      },
      mspId: 'Org1MSP',
      type: 'X.509',
    };
    await wallet.put('admin', x509Identity);
    logger.info('Successfully enrolled admin user "admin" and imported it into the wallet');

  } catch (error) {
    let errMessage = 'Failed to enroll admin user "admin": ' + error;
    logger.error(errMessage);
  }
}

let enrollAppUser = async function() {
  try {
    // load the network configuration
    const ccpPath = path.resolve(__dirname, '..', '..', '..', 'fabric-samples', networkScale, 'organizations', 'peerOrganizations', 'org1.example.com', 'connection-org1.json');
    const ccp = JSON.parse(fs.readFileSync(ccpPath, 'utf8'));

    // Create a new CA client for interacting with the CA.
    const caURL = ccp.certificateAuthorities['ca.org1.example.com'].url;
    const ca = new FabricCAServices(caURL);

    // Create a new file system based wallet for managing identities.
    const walletPath = path.join(__dirname, 'wallet');
    const wallet = await Wallets.newFileSystemWallet(walletPath);
    logger.info(`Wallet path: ${walletPath}`);

    // Check to see if we've already enrolled the user.
    const userIdentity = await wallet.get('appUser');
    if (userIdentity) {
      logger.info('An identity for the user "appUser" already exists in the wallet');
      return;
    }

    // Check to see if we've already enrolled the admin user.
    let adminIdentity = await wallet.get('admin');
    if (!adminIdentity) {
      logger.info('An identity for the user "admin" does not exist in the wallet, enroll it now...');
      await enrollAdmin();
      adminIdentity = await wallet.get('admin');
      if (!adminIdentity) {
        logger.error('An identity for the user "admin" enroll failed, stop request.');
        return;
      }
    }

    // build a user object for authenticating with the CA
    const provider = wallet.getProviderRegistry().getProvider(adminIdentity.type);
    const adminUser = await provider.getUserContext(adminIdentity, 'admin');

    // Register the user, enroll the user, and import the new identity into the wallet.
    const secret = await ca.register({
      affiliation: 'org1.department1',
      enrollmentID: 'appUser',
      role: 'client'
    }, adminUser);
    const enrollment = await ca.enroll({
      enrollmentID: 'appUser',
      enrollmentSecret: secret
    });
    const x509Identity = {
      credentials: {
        certificate: enrollment.certificate,
        privateKey: enrollment.key.toBytes(),
      },
      mspId: 'Org1MSP',
      type: 'X.509',
    };
    await wallet.put('appUser', x509Identity);
    logger.info('Successfully registered and enrolled admin user "appUser" and imported it into the wallet');

  } catch (error) {
    let errMessage = 'Failed to register user "appUser" ' + error;
    logger.error(errMessage);
  }
}


router.post('/invoke/:channelName/:chaincodeName', async function (req, res) {
  let channelName = req.params.channelName;
  let chaincodeName = req.params.chaincodeName;
  let body = req.body;
  if (body.message === 'prepare') {
    logger.info("Received request type: prepare")
    await invoke(res, channelName, chaincodeName, 'Prepare', JSON.stringify(req.body));
  }
  else if (body.message === 'train') {
    logger.info("Received request type: train")
    await invoke(res, channelName, chaincodeName,'Train', JSON.stringify(req.body));
  }
  else if (body.message === 'train_ready') {
    logger.info("Received request type: train_ready")
    await invoke(res, channelName, chaincodeName,'TrainReady', JSON.stringify(req.body));
  }
  else if (body.message === 'w_glob') {
    logger.info("Received request type: w_glob")
    await invoke(res, channelName, chaincodeName,'WGlob', JSON.stringify(req.body));
  }
  else if (body.message === 'negotiate') {
    logger.info("Received request type: negotiate")
    await invoke(res, channelName, chaincodeName, 'Negotiate', JSON.stringify(req.body));
  }
  else if (body.message === 'negotiate_ready') {
    logger.info("Received request type: negotiate_ready")
    await invoke(res, channelName, chaincodeName, 'NegotiateReady', JSON.stringify(req.body));
  }
  else
    common.responseBadRequestError(res, 'No such request: ' + body.message);
});


router.post('/test/echo', async function (req, res) {
  common.responseSuccess(res, req.body);
});

let invoke = async function(res, channelName, chaincodeName, invokeFuncName, args) {
  let maxTries = 30;
  let errMessage;
  while (maxTries>0) {
    try {
      await submitRequest(channelName, chaincodeName, invokeFuncName, args);
      common.responseSuccess(res, {});
      return;
    } catch (error) {
      errMessage = 'Failed to submit transaction: ' + error;
      // if dirty read happened, retry for 3 times
      if (errMessage.indexOf('READ_CONFLICT') !== -1 || errMessage.indexOf('ENDORSEMENT_POLICY_FAILURE') !== -1 ||
      errMessage.indexOf('constructing descriptor for chaincodes')) {
        maxTries--;
      } else {
        maxTries=0;
      }
    }
  }
  common.responseInternalError(res, errMessage);
};

let submitRequest = async function (channelName, chaincodeName, invokeFuncName, args) {
  // load the network configuration
  const ccpPath = path.resolve(__dirname, '..', '..', '..', 'fabric-samples', networkScale, 'organizations', 'peerOrganizations', 'org1.example.com', 'connection-org1.json');
  const fileExists = fs.existsSync(ccpPath);
  if (!fileExists) {
    throw new Error(`no such file or directory: ${ccpPath}`);
  }
  let ccp = JSON.parse(fs.readFileSync(ccpPath, 'utf8'));

  // Create a new file system based wallet for managing identities.
  const walletPath = path.join(__dirname, 'wallet');
  const wallet = await Wallets.newFileSystemWallet(walletPath);
  logger.debug(`Wallet path: ${walletPath}`);

  // Check to see if we've already enrolled the user.
  let identity = await wallet.get('appUser');
  if (!identity) {
    logger.info('An identity for the user "appUser" does not exist in the wallet, enroll it now...');
    await enrollAppUser();
    identity = await wallet.get('appUser');
    if (!identity) {
      logger.error('An identity for the user "appUser" enroll failed, stop request.');
      return;
    }
  }

  // Create a new gateway for connecting to our peer node.
  const gateway = new Gateway();
  await gateway.connect(ccp, { wallet, identity: 'appUser', discovery: { enabled: true, asLocalhost: true } });

  // Get the network (channel) our contract is deployed to.
  const network = await gateway.getNetwork(channelName);

  // Get the contract from the network.
  const contract = network.getContract(chaincodeName);

  // Submit the specified transaction.
  await contract.submitTransaction(invokeFuncName, args);
  logger.info('Transaction has been submitted: ' + invokeFuncName);

  // Disconnect from the gateway.
  await gateway.disconnect();
}

module.exports = router;
