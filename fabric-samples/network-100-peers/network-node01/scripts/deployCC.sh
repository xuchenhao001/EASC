
CHANNEL_NAME="$1"
CC_SRC_LANGUAGE="$2"
VERSION="$3"
DELAY="$4"
MAX_RETRY="$5"
VERBOSE="$6"
: ${CHANNEL_NAME:="mychannel"}
: ${CC_SRC_LANGUAGE:="golang"}
: ${VERSION:="1"}
: ${DELAY:="3"}
: ${MAX_RETRY:="5"}
: ${VERBOSE:="false"}
CC_SRC_LANGUAGE=`echo "$CC_SRC_LANGUAGE" | tr [:upper:] [:lower:]`

FABRIC_CFG_PATH=$PWD/../configtx/

if [ "$CC_SRC_LANGUAGE" = "go" -o "$CC_SRC_LANGUAGE" = "golang" ] ; then
	CC_RUNTIME_LANGUAGE=golang
	CC_SRC_PATH="../../chaincode/fabcar/go/"

	echo Vendoring Go dependencies ...
	pushd ../../chaincode/fabcar/go
	GO111MODULE=on go mod vendor
	popd
	echo Finished vendoring Go dependencies

elif [ "$CC_SRC_LANGUAGE" = "javascript" ]; then
	CC_RUNTIME_LANGUAGE=node # chaincode runtime language is node.js
	CC_SRC_PATH="../chaincode/fabcar/javascript/"

elif [ "$CC_SRC_LANGUAGE" = "java" ]; then
	CC_RUNTIME_LANGUAGE=java
	CC_SRC_PATH="../chaincode/fabcar/java/build/install/fabcar"

	echo Compiling Java code ...
	pushd ../chaincode/fabcar/java
	./gradlew installDist
	popd
	echo Finished compiling Java code

elif [ "$CC_SRC_LANGUAGE" = "typescript" ]; then
	CC_RUNTIME_LANGUAGE=node # chaincode runtime language is node.js
	CC_SRC_PATH="../chaincode/fabcar/typescript/"

	echo Compiling TypeScript code into JavaScript ...
	pushd ../chaincode/fabcar/typescript
	npm install
	npm run build
	popd
	echo Finished compiling TypeScript code into JavaScript

else
	echo The chaincode language ${CC_SRC_LANGUAGE} is not supported by this script
	echo Supported chaincode languages are: go, java, javascript, and typescript
	exit 1
fi

# import utils
. scripts/envVar.sh


packageChaincode() {
  ORG=$1
  setGlobals $ORG
  set -x
  peer lifecycle chaincode package fabcar.tar.gz --path ${CC_SRC_PATH} --lang ${CC_RUNTIME_LANGUAGE} --label fabcar_${VERSION} >&log.txt
  res=$?
  set +x
  cat log.txt
  verifyResult $res "Chaincode packaging on peer0.org${ORG} has failed"
  echo "===================== Chaincode is packaged on peer0.org${ORG} ===================== "
  echo
}

# installChaincode PEER ORG
installChaincode() {
  ORG=$1
  setGlobals $ORG
  set -x
  peer lifecycle chaincode install fabcar.tar.gz >&log.txt
  res=$?
  set +x
  cat log.txt
  verifyResult $res "Chaincode installation on peer0.org${ORG} has failed"
  echo "===================== Chaincode is installed on peer0.org${ORG} ===================== "
  echo
}

# queryInstalled PEER ORG
queryInstalled() {
  ORG=$1
  setGlobals $ORG
  set -x
  peer lifecycle chaincode queryinstalled >&log.txt
  res=$?
  set +x
  cat log.txt
	PACKAGE_ID=$(sed -n "/fabcar_${VERSION}/{s/^Package ID: //; s/, Label:.*$//; p;}" log.txt)
  verifyResult $res "Query installed on peer0.org${ORG} has failed"
  echo "===================== Query installed successful on peer0.org${ORG} on channel ===================== "
  echo
}

# approveForMyOrg VERSION PEER ORG
approveForMyOrg() {
  ORG=$1
  setGlobals $ORG
  set -x
  peer lifecycle chaincode approveformyorg --signature-policy $SIGNATURE_POLICY -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile $ORDERER_CA --channelID $CHANNEL_NAME --name fabcar --version ${VERSION} --init-required --package-id ${PACKAGE_ID} --sequence ${VERSION} >&log.txt
  set +x
  cat log.txt
  verifyResult $res "Chaincode definition approved on peer0.org${ORG} on channel '$CHANNEL_NAME' failed"
  echo "===================== Chaincode definition approved on peer0.org${ORG} on channel '$CHANNEL_NAME' ===================== "
  echo
}

# checkCommitReadiness VERSION PEER ORG
checkCommitReadiness() {
  ORG=$1
  shift 1
  setGlobals $ORG
  echo "===================== Checking the commit readiness of the chaincode definition on peer0.org${ORG} on channel '$CHANNEL_NAME'... ===================== "
	local rc=1
	local COUNTER=1
	# continue to poll
  # we either get a successful response, or reach MAX RETRY
	while [ $rc -ne 0 -a $COUNTER -lt $MAX_RETRY ] ; do
    sleep $DELAY
    echo "Attempting to check the commit readiness of the chaincode definition on peer0.org${ORG}, Retry after $DELAY seconds."
    set -x
    peer lifecycle chaincode checkcommitreadiness --signature-policy $SIGNATURE_POLICY --channelID $CHANNEL_NAME --name fabcar --version ${VERSION} --sequence ${VERSION} --output json --init-required >&log.txt
    res=$?
    set +x
    let rc=0
    for var in "$@"
    do
      grep "$var" log.txt &>/dev/null || let rc=1
    done
		COUNTER=$(expr $COUNTER + 1)
	done
  cat log.txt
  if test $rc -eq 0; then
    echo "===================== Checking the commit readiness of the chaincode definition successful on peer0.org${ORG} on channel '$CHANNEL_NAME' ===================== "
  else
    echo "!!!!!!!!!!!!!!! After $MAX_RETRY attempts, Check commit readiness result on peer0.org${ORG} is INVALID !!!!!!!!!!!!!!!!"
    echo
    exit 1
  fi
}

# commitChaincodeDefinition VERSION PEER ORG (PEER ORG)...
commitChaincodeDefinition() {
  parsePeerConnectionParameters $@
  res=$?
  verifyResult $res "Invoke transaction failed on channel '$CHANNEL_NAME' due to uneven number of peer and org parameters "

  # while 'peer chaincode' command can get the orderer endpoint from the
  # peer (if join was successful), let's supply it directly as we know
  # it using the "-o" option
  set -x
  peer lifecycle chaincode commit --signature-policy $SIGNATURE_POLICY -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile $ORDERER_CA --channelID $CHANNEL_NAME --name fabcar $PEER_CONN_PARMS --version ${VERSION} --sequence ${VERSION} --init-required >&log.txt
  res=$?
  set +x
  cat log.txt
  verifyResult $res "Chaincode definition commit failed on peer0.org${ORG} on channel '$CHANNEL_NAME' failed"
  echo "===================== Chaincode definition committed on channel '$CHANNEL_NAME' ===================== "
  echo
}

# queryCommitted ORG
queryCommitted() {
  ORG=$1
  setGlobals $ORG
  EXPECTED_RESULT="Version: ${VERSION}, Sequence: ${VERSION}, Endorsement Plugin: escc, Validation Plugin: vscc"
  echo "===================== Querying chaincode definition on peer0.org${ORG} on channel '$CHANNEL_NAME'... ===================== "
	local rc=1
	local COUNTER=1
	# continue to poll
  # we either get a successful response, or reach MAX RETRY
	while [ $rc -ne 0 -a $COUNTER -lt $MAX_RETRY ] ; do
    sleep $DELAY
    echo "Attempting to Query committed status on peer0.org${ORG}, Retry after $DELAY seconds."
    set -x
    peer lifecycle chaincode querycommitted --channelID $CHANNEL_NAME --name fabcar >&log.txt
    res=$?
    set +x
		test $res -eq 0 && VALUE=$(cat log.txt | grep -o '^Version: [0-9], Sequence: [0-9], Endorsement Plugin: escc, Validation Plugin: vscc')
    test "$VALUE" = "$EXPECTED_RESULT" && let rc=0
		COUNTER=$(expr $COUNTER + 1)
	done
  echo
  cat log.txt
  if test $rc -eq 0; then
    echo "===================== Query chaincode definition successful on peer0.org${ORG} on channel '$CHANNEL_NAME' ===================== "
		echo
  else
    echo "!!!!!!!!!!!!!!! After $MAX_RETRY attempts, Query chaincode definition result on peer0.org${ORG} is INVALID !!!!!!!!!!!!!!!!"
    echo
    exit 1
  fi
}

chaincodeInvokeInit() {
  parsePeerConnectionParameters $@
  res=$?
  verifyResult $res "Invoke transaction failed on channel '$CHANNEL_NAME' due to uneven number of peer and org parameters "

  # while 'peer chaincode' command can get the orderer endpoint from the
  # peer (if join was successful), let's supply it directly as we know
  # it using the "-o" option
  set -x
  peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile $ORDERER_CA -C $CHANNEL_NAME -n fabcar $PEER_CONN_PARMS --isInit -c '{"function":"initLedger","Args":[]}' >&log.txt
  res=$?
  set +x
  cat log.txt
  verifyResult $res "Invoke execution on $PEERS failed "
  echo "===================== Invoke transaction successful on $PEERS on channel '$CHANNEL_NAME' ===================== "
  echo
}

chaincodeQuery() {
  ORG=$1
  setGlobals $ORG
  echo "===================== Querying on peer0.org${ORG} on channel '$CHANNEL_NAME'... ===================== "
	local rc=1
	local COUNTER=1
	# continue to poll
  # we either get a successful response, or reach MAX RETRY
	while [ $rc -ne 0 -a $COUNTER -lt $MAX_RETRY ] ; do
    sleep $DELAY
    echo "Attempting to Query peer0.org${ORG}, Retry after $DELAY seconds."
    set -x
    peer chaincode query -C $CHANNEL_NAME -n fabcar -c '{"Args":["queryAllCars"]}' >&log.txt
    res=$?
    set +x
		let rc=$res
		COUNTER=$(expr $COUNTER + 1)
	done
  echo
  cat log.txt
  if test $rc -eq 0; then
    echo "===================== Query successful on peer0.org${ORG} on channel '$CHANNEL_NAME' ===================== "
		echo
  else
    echo "!!!!!!!!!!!!!!! After $MAX_RETRY attempts, Query result on peer0.org${ORG} is INVALID !!!!!!!!!!!!!!!!"
    echo
    exit 1
  fi
}

SIGNATURE_POLICY="AND('Org1MSP.member','Org2MSP.member','Org3MSP.member','Org4MSP.member','Org5MSP.member','Org6MSP.member','Org7MSP.member','Org8MSP.member','Org9MSP.member','Org10MSP.member','Org11MSP.member','Org12MSP.member','Org13MSP.member','Org14MSP.member','Org15MSP.member','Org16MSP.member','Org17MSP.member','Org18MSP.member','Org19MSP.member','Org20MSP.member','Org21MSP.member','Org22MSP.member','Org23MSP.member','Org24MSP.member','Org25MSP.member','Org26MSP.member','Org27MSP.member','Org28MSP.member','Org29MSP.member','Org30MSP.member','Org31MSP.member','Org32MSP.member','Org33MSP.member','Org34MSP.member','Org35MSP.member','Org36MSP.member','Org37MSP.member','Org38MSP.member','Org39MSP.member','Org40MSP.member','Org41MSP.member','Org42MSP.member','Org43MSP.member','Org44MSP.member','Org45MSP.member','Org46MSP.member','Org47MSP.member','Org48MSP.member','Org49MSP.member','Org50MSP.member','Org51MSP.member','Org52MSP.member','Org53MSP.member','Org54MSP.member','Org55MSP.member','Org56MSP.member','Org57MSP.member','Org58MSP.member','Org59MSP.member','Org60MSP.member','Org61MSP.member','Org62MSP.member','Org63MSP.member','Org64MSP.member','Org65MSP.member','Org66MSP.member','Org67MSP.member','Org68MSP.member','Org69MSP.member','Org70MSP.member','Org71MSP.member','Org72MSP.member','Org73MSP.member','Org74MSP.member','Org75MSP.member','Org76MSP.member','Org77MSP.member','Org78MSP.member','Org79MSP.member','Org80MSP.member','Org81MSP.member','Org82MSP.member','Org83MSP.member','Org84MSP.member','Org85MSP.member','Org86MSP.member','Org87MSP.member','Org88MSP.member','Org89MSP.member','Org90MSP.member','Org91MSP.member','Org92MSP.member','Org93MSP.member','Org94MSP.member','Org95MSP.member','Org96MSP.member','Org97MSP.member','Org98MSP.member','Org99MSP.member','Org100MSP.member')"

## at first we package the chaincode
packageChaincode 1

## Install chaincode on peer0.org1 and peer0.org2
echo "Installing chaincode on peers..."
installChaincode 1
installChaincode 2
installChaincode 3
installChaincode 4
installChaincode 5
installChaincode 6
installChaincode 7
installChaincode 8
installChaincode 9
installChaincode 10
installChaincode 11
installChaincode 12
installChaincode 13
installChaincode 14
installChaincode 15
installChaincode 16
installChaincode 17
installChaincode 18
installChaincode 19
installChaincode 20
installChaincode 21
installChaincode 22
installChaincode 23
installChaincode 24
installChaincode 25
installChaincode 26
installChaincode 27
installChaincode 28
installChaincode 29
installChaincode 30
installChaincode 31
installChaincode 32
installChaincode 33
installChaincode 34
installChaincode 35
installChaincode 36
installChaincode 37
installChaincode 38
installChaincode 39
installChaincode 40
installChaincode 41
installChaincode 42
installChaincode 43
installChaincode 44
installChaincode 45
installChaincode 46
installChaincode 47
installChaincode 48
installChaincode 49
installChaincode 50
installChaincode 51
installChaincode 52
installChaincode 53
installChaincode 54
installChaincode 55
installChaincode 56
installChaincode 57
installChaincode 58
installChaincode 59
installChaincode 60
installChaincode 61
installChaincode 62
installChaincode 63
installChaincode 64
installChaincode 65
installChaincode 66
installChaincode 67
installChaincode 68
installChaincode 69
installChaincode 70
installChaincode 71
installChaincode 72
installChaincode 73
installChaincode 74
installChaincode 75
installChaincode 76
installChaincode 77
installChaincode 78
installChaincode 79
installChaincode 80
installChaincode 81
installChaincode 82
installChaincode 83
installChaincode 84
installChaincode 85
installChaincode 86
installChaincode 87
installChaincode 88
installChaincode 89
installChaincode 90
installChaincode 91
installChaincode 92
installChaincode 93
installChaincode 94
installChaincode 95
installChaincode 96
installChaincode 97
installChaincode 98
installChaincode 99
installChaincode 100

## query whether the chaincode is installed
queryInstalled 1

## approve the definition for org
approveForMyOrg 1
checkCommitReadiness 1 "\"Org1MSP\": true"
approveForMyOrg 2
checkCommitReadiness 2 "\"Org2MSP\": true"
approveForMyOrg 3
checkCommitReadiness 3 "\"Org3MSP\": true"
approveForMyOrg 4
checkCommitReadiness 4 "\"Org4MSP\": true"
approveForMyOrg 5
checkCommitReadiness 5 "\"Org5MSP\": true"
approveForMyOrg 6
checkCommitReadiness 6 "\"Org6MSP\": true"
approveForMyOrg 7
checkCommitReadiness 7 "\"Org7MSP\": true"
approveForMyOrg 8
checkCommitReadiness 8 "\"Org8MSP\": true"
approveForMyOrg 9
checkCommitReadiness 9 "\"Org9MSP\": true"
approveForMyOrg 10
checkCommitReadiness 10 "\"Org10MSP\": true"
approveForMyOrg 11
checkCommitReadiness 11 "\"Org11MSP\": true"
approveForMyOrg 12
checkCommitReadiness 12 "\"Org12MSP\": true"
approveForMyOrg 13
checkCommitReadiness 13 "\"Org13MSP\": true"
approveForMyOrg 14
checkCommitReadiness 14 "\"Org14MSP\": true"
approveForMyOrg 15
checkCommitReadiness 15 "\"Org15MSP\": true"
approveForMyOrg 16
checkCommitReadiness 16 "\"Org16MSP\": true"
approveForMyOrg 17
checkCommitReadiness 17 "\"Org17MSP\": true"
approveForMyOrg 18
checkCommitReadiness 18 "\"Org18MSP\": true"
approveForMyOrg 19
checkCommitReadiness 19 "\"Org19MSP\": true"
approveForMyOrg 20
checkCommitReadiness 20 "\"Org20MSP\": true"
approveForMyOrg 21
checkCommitReadiness 21 "\"Org21MSP\": true"
approveForMyOrg 22
checkCommitReadiness 22 "\"Org22MSP\": true"
approveForMyOrg 23
checkCommitReadiness 23 "\"Org23MSP\": true"
approveForMyOrg 24
checkCommitReadiness 24 "\"Org24MSP\": true"
approveForMyOrg 25
checkCommitReadiness 25 "\"Org25MSP\": true"
approveForMyOrg 26
checkCommitReadiness 26 "\"Org26MSP\": true"
approveForMyOrg 27
checkCommitReadiness 27 "\"Org27MSP\": true"
approveForMyOrg 28
checkCommitReadiness 28 "\"Org28MSP\": true"
approveForMyOrg 29
checkCommitReadiness 29 "\"Org29MSP\": true"
approveForMyOrg 30
checkCommitReadiness 30 "\"Org30MSP\": true"
approveForMyOrg 31
checkCommitReadiness 31 "\"Org31MSP\": true"
approveForMyOrg 32
checkCommitReadiness 32 "\"Org32MSP\": true"
approveForMyOrg 33
checkCommitReadiness 33 "\"Org33MSP\": true"
approveForMyOrg 34
checkCommitReadiness 34 "\"Org34MSP\": true"
approveForMyOrg 35
checkCommitReadiness 35 "\"Org35MSP\": true"
approveForMyOrg 36
checkCommitReadiness 36 "\"Org36MSP\": true"
approveForMyOrg 37
checkCommitReadiness 37 "\"Org37MSP\": true"
approveForMyOrg 38
checkCommitReadiness 38 "\"Org38MSP\": true"
approveForMyOrg 39
checkCommitReadiness 39 "\"Org39MSP\": true"
approveForMyOrg 40
checkCommitReadiness 40 "\"Org40MSP\": true"
approveForMyOrg 41
checkCommitReadiness 41 "\"Org41MSP\": true"
approveForMyOrg 42
checkCommitReadiness 42 "\"Org42MSP\": true"
approveForMyOrg 43
checkCommitReadiness 43 "\"Org43MSP\": true"
approveForMyOrg 44
checkCommitReadiness 44 "\"Org44MSP\": true"
approveForMyOrg 45
checkCommitReadiness 45 "\"Org45MSP\": true"
approveForMyOrg 46
checkCommitReadiness 46 "\"Org46MSP\": true"
approveForMyOrg 47
checkCommitReadiness 47 "\"Org47MSP\": true"
approveForMyOrg 48
checkCommitReadiness 48 "\"Org48MSP\": true"
approveForMyOrg 49
checkCommitReadiness 49 "\"Org49MSP\": true"
approveForMyOrg 50
checkCommitReadiness 50 "\"Org50MSP\": true"
approveForMyOrg 51
checkCommitReadiness 51 "\"Org51MSP\": true"
approveForMyOrg 52
checkCommitReadiness 52 "\"Org52MSP\": true"
approveForMyOrg 53
checkCommitReadiness 53 "\"Org53MSP\": true"
approveForMyOrg 54
checkCommitReadiness 54 "\"Org54MSP\": true"
approveForMyOrg 55
checkCommitReadiness 55 "\"Org55MSP\": true"
approveForMyOrg 56
checkCommitReadiness 56 "\"Org56MSP\": true"
approveForMyOrg 57
checkCommitReadiness 57 "\"Org57MSP\": true"
approveForMyOrg 58
checkCommitReadiness 58 "\"Org58MSP\": true"
approveForMyOrg 59
checkCommitReadiness 59 "\"Org59MSP\": true"
approveForMyOrg 60
checkCommitReadiness 60 "\"Org60MSP\": true"
approveForMyOrg 61
checkCommitReadiness 61 "\"Org61MSP\": true"
approveForMyOrg 62
checkCommitReadiness 62 "\"Org62MSP\": true"
approveForMyOrg 63
checkCommitReadiness 63 "\"Org63MSP\": true"
approveForMyOrg 64
checkCommitReadiness 64 "\"Org64MSP\": true"
approveForMyOrg 65
checkCommitReadiness 65 "\"Org65MSP\": true"
approveForMyOrg 66
checkCommitReadiness 66 "\"Org66MSP\": true"
approveForMyOrg 67
checkCommitReadiness 67 "\"Org67MSP\": true"
approveForMyOrg 68
checkCommitReadiness 68 "\"Org68MSP\": true"
approveForMyOrg 69
checkCommitReadiness 69 "\"Org69MSP\": true"
approveForMyOrg 70
checkCommitReadiness 70 "\"Org70MSP\": true"
approveForMyOrg 71
checkCommitReadiness 71 "\"Org71MSP\": true"
approveForMyOrg 72
checkCommitReadiness 72 "\"Org72MSP\": true"
approveForMyOrg 73
checkCommitReadiness 73 "\"Org73MSP\": true"
approveForMyOrg 74
checkCommitReadiness 74 "\"Org74MSP\": true"
approveForMyOrg 75
checkCommitReadiness 75 "\"Org75MSP\": true"
approveForMyOrg 76
checkCommitReadiness 76 "\"Org76MSP\": true"
approveForMyOrg 77
checkCommitReadiness 77 "\"Org77MSP\": true"
approveForMyOrg 78
checkCommitReadiness 78 "\"Org78MSP\": true"
approveForMyOrg 79
checkCommitReadiness 79 "\"Org79MSP\": true"
approveForMyOrg 80
checkCommitReadiness 80 "\"Org80MSP\": true"
approveForMyOrg 81
checkCommitReadiness 81 "\"Org81MSP\": true"
approveForMyOrg 82
checkCommitReadiness 82 "\"Org82MSP\": true"
approveForMyOrg 83
checkCommitReadiness 83 "\"Org83MSP\": true"
approveForMyOrg 84
checkCommitReadiness 84 "\"Org84MSP\": true"
approveForMyOrg 85
checkCommitReadiness 85 "\"Org85MSP\": true"
approveForMyOrg 86
checkCommitReadiness 86 "\"Org86MSP\": true"
approveForMyOrg 87
checkCommitReadiness 87 "\"Org87MSP\": true"
approveForMyOrg 88
checkCommitReadiness 88 "\"Org88MSP\": true"
approveForMyOrg 89
checkCommitReadiness 89 "\"Org89MSP\": true"
approveForMyOrg 90
checkCommitReadiness 90 "\"Org90MSP\": true"
approveForMyOrg 91
checkCommitReadiness 91 "\"Org91MSP\": true"
approveForMyOrg 92
checkCommitReadiness 92 "\"Org92MSP\": true"
approveForMyOrg 93
checkCommitReadiness 93 "\"Org93MSP\": true"
approveForMyOrg 94
checkCommitReadiness 94 "\"Org94MSP\": true"
approveForMyOrg 95
checkCommitReadiness 95 "\"Org95MSP\": true"
approveForMyOrg 96
checkCommitReadiness 96 "\"Org96MSP\": true"
approveForMyOrg 97
checkCommitReadiness 97 "\"Org97MSP\": true"
approveForMyOrg 98
checkCommitReadiness 98 "\"Org98MSP\": true"
approveForMyOrg 99
checkCommitReadiness 99 "\"Org99MSP\": true"
approveForMyOrg 100
checkCommitReadiness 100 "\"Org100MSP\": true"

## now that we know for sure both orgs have approved, commit the definition
commitChaincodeDefinition 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100

## query on both orgs to see that the definition committed successfully
queryCommitted 1
queryCommitted 2
queryCommitted 3
queryCommitted 4
queryCommitted 5
queryCommitted 6
queryCommitted 7
queryCommitted 8
queryCommitted 9
queryCommitted 10
queryCommitted 11
queryCommitted 12
queryCommitted 13
queryCommitted 14
queryCommitted 15
queryCommitted 16
queryCommitted 17
queryCommitted 18
queryCommitted 19
queryCommitted 20
queryCommitted 21
queryCommitted 22
queryCommitted 23
queryCommitted 24
queryCommitted 25
queryCommitted 26
queryCommitted 27
queryCommitted 28
queryCommitted 29
queryCommitted 30
queryCommitted 31
queryCommitted 32
queryCommitted 33
queryCommitted 34
queryCommitted 35
queryCommitted 36
queryCommitted 37
queryCommitted 38
queryCommitted 39
queryCommitted 40
queryCommitted 41
queryCommitted 42
queryCommitted 43
queryCommitted 44
queryCommitted 45
queryCommitted 46
queryCommitted 47
queryCommitted 48
queryCommitted 49
queryCommitted 50
queryCommitted 51
queryCommitted 52
queryCommitted 53
queryCommitted 54
queryCommitted 55
queryCommitted 56
queryCommitted 57
queryCommitted 58
queryCommitted 59
queryCommitted 60
queryCommitted 61
queryCommitted 62
queryCommitted 63
queryCommitted 64
queryCommitted 65
queryCommitted 66
queryCommitted 67
queryCommitted 68
queryCommitted 69
queryCommitted 70
queryCommitted 71
queryCommitted 72
queryCommitted 73
queryCommitted 74
queryCommitted 75
queryCommitted 76
queryCommitted 77
queryCommitted 78
queryCommitted 79
queryCommitted 80
queryCommitted 81
queryCommitted 82
queryCommitted 83
queryCommitted 84
queryCommitted 85
queryCommitted 86
queryCommitted 87
queryCommitted 88
queryCommitted 89
queryCommitted 90
queryCommitted 91
queryCommitted 92
queryCommitted 93
queryCommitted 94
queryCommitted 95
queryCommitted 96
queryCommitted 97
queryCommitted 98
queryCommitted 99
queryCommitted 100

## Invoke the chaincode
chaincodeInvokeInit 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100

sleep 10

# Query chaincode on peer0.org1
# echo "Querying chaincode on peer0.org1..."
# chaincodeQuery 1

exit 0

