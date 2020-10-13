#!/bin/bash


CHANNEL_NAME="$1"
DELAY="$2"
MAX_RETRY="$3"
VERBOSE="$4"
: ${CHANNEL_NAME:="mychannel"}
: ${DELAY:="3"}
: ${MAX_RETRY:="5"}
: ${VERBOSE:="false"}

# import utils
. scripts/envVar.sh

if [ ! -d "channel-artifacts" ]; then
	mkdir channel-artifacts
fi

createChannelTx() {

	set -x
	configtxgen -profile TwoOrgsChannel -outputCreateChannelTx ./channel-artifacts/${CHANNEL_NAME}.tx -channelID $CHANNEL_NAME
	res=$?
	set +x
	if [ $res -ne 0 ]; then
		echo "Failed to generate channel configuration transaction..."
		exit 1
	fi
	echo

}

createAncorPeerTx() {
	ORGMSP=$1

	echo "#######    Generating anchor peer update transaction for ${ORGMSP}  ##########"
	set -x
	configtxgen -profile TwoOrgsChannel -outputAnchorPeersUpdate ./channel-artifacts/${ORGMSP}anchors.tx -channelID $CHANNEL_NAME -asOrg ${ORGMSP}
	res=$?
	set +x
	if [ $res -ne 0 ]; then
		echo "Failed to generate anchor peer update transaction for ${ORGMSP}..."
		exit 1
	fi
	echo
}

createChannel() {
	setGlobals 1
	# Poll in case the raft leader is not set yet
	local rc=1
	local COUNTER=1
	while [ $rc -ne 0 -a $COUNTER -lt $MAX_RETRY ] ; do
		sleep $DELAY
		set -x
		peer channel create -o localhost:7050 -c $CHANNEL_NAME --ordererTLSHostnameOverride orderer.example.com -f ./channel-artifacts/${CHANNEL_NAME}.tx --outputBlock ./channel-artifacts/${CHANNEL_NAME}.block --tls --cafile $ORDERER_CA >&log.txt
		res=$?
		set +x
		let rc=$res
		COUNTER=$(expr $COUNTER + 1)
	done
	cat log.txt
	verifyResult $res "Channel creation failed"
	echo
	echo "===================== Channel '$CHANNEL_NAME' created ===================== "
	echo
}

# queryCommitted ORG
joinChannel() {
  ORG=$1
  setGlobals $ORG
	local rc=1
	local COUNTER=1
	## Sometimes Join takes time, hence retry
	while [ $rc -ne 0 -a $COUNTER -lt $MAX_RETRY ] ; do
    sleep $DELAY
    set -x
    peer channel join -b ./channel-artifacts/$CHANNEL_NAME.block >&log.txt
    res=$?
    set +x
		let rc=$res
		COUNTER=$(expr $COUNTER + 1)
	done
	cat log.txt
	echo
	verifyResult $res "After $MAX_RETRY attempts, peer0.org${ORG} has failed to join channel '$CHANNEL_NAME' "
}

updateAnchorPeers() {
  ORG=$1
  setGlobals $ORG
	local rc=1
	local COUNTER=1
	## Sometimes Join takes time, hence retry
	while [ $rc -ne 0 -a $COUNTER -lt $MAX_RETRY ] ; do
    sleep $DELAY
    set -x
		peer channel update -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com -c $CHANNEL_NAME -f ./channel-artifacts/${CORE_PEER_LOCALMSPID}anchors.tx --tls --cafile $ORDERER_CA >&log.txt
    res=$?
    set +x
		let rc=$res
		COUNTER=$(expr $COUNTER + 1)
	done
	cat log.txt
  verifyResult $res "Anchor peer update failed"
  echo "===================== Anchor peers updated for org '$CORE_PEER_LOCALMSPID' on channel '$CHANNEL_NAME' ===================== "
  sleep $DELAY
  echo
}

verifyResult() {
  if [ $1 -ne 0 ]; then
    echo "!!!!!!!!!!!!!!! "$2" !!!!!!!!!!!!!!!!"
    echo
    exit 1
  fi
}

FABRIC_CFG_PATH=${PWD}/configtx

## Create channeltx
echo "### Generating channel create transaction '${CHANNEL_NAME}.tx' ###"
createChannelTx

## Create anchorpeertx
echo "### Generating anchor peer update transactions ###"
createAncorPeerTx Org1MSP
createAncorPeerTx Org2MSP
createAncorPeerTx Org3MSP
createAncorPeerTx Org4MSP
createAncorPeerTx Org5MSP
createAncorPeerTx Org6MSP
createAncorPeerTx Org7MSP
createAncorPeerTx Org8MSP
createAncorPeerTx Org9MSP
createAncorPeerTx Org10MSP
createAncorPeerTx Org11MSP
createAncorPeerTx Org12MSP
createAncorPeerTx Org13MSP
createAncorPeerTx Org14MSP
createAncorPeerTx Org15MSP
createAncorPeerTx Org16MSP
createAncorPeerTx Org17MSP
createAncorPeerTx Org18MSP
createAncorPeerTx Org19MSP
createAncorPeerTx Org20MSP

# FABRIC_CFG_PATH=$PWD/../config/

## Create channel
echo "Creating channel "$CHANNEL_NAME
createChannel

## Join all the peers to the channel
echo "Join Org peers to the channel..."
joinChannel 1
joinChannel 2
joinChannel 3
joinChannel 4
joinChannel 5
joinChannel 6
joinChannel 7
joinChannel 8
joinChannel 9
joinChannel 10
joinChannel 11
joinChannel 12
joinChannel 13
joinChannel 14
joinChannel 15
joinChannel 16
joinChannel 17
joinChannel 18
joinChannel 19
joinChannel 20

## Set the anchor peers for each org in the channel
echo "Updating anchor peers for orgs..."
updateAnchorPeers 1
updateAnchorPeers 2
updateAnchorPeers 3
updateAnchorPeers 4
updateAnchorPeers 5
updateAnchorPeers 6
updateAnchorPeers 7
updateAnchorPeers 8
updateAnchorPeers 9
updateAnchorPeers 10
updateAnchorPeers 11
updateAnchorPeers 12
updateAnchorPeers 13
updateAnchorPeers 14
updateAnchorPeers 15
updateAnchorPeers 16
updateAnchorPeers 17
updateAnchorPeers 18
updateAnchorPeers 19
updateAnchorPeers 20

echo
echo "========= Channel successfully joined =========== "
echo

exit 0