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
	echo $FABRIC_CFG_PATH
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

FABRIC_CFG_PATH=${PWD}/../configtx

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
createAncorPeerTx Org21MSP
createAncorPeerTx Org22MSP
createAncorPeerTx Org23MSP
createAncorPeerTx Org24MSP
createAncorPeerTx Org25MSP
createAncorPeerTx Org26MSP
createAncorPeerTx Org27MSP
createAncorPeerTx Org28MSP
createAncorPeerTx Org29MSP
createAncorPeerTx Org30MSP
createAncorPeerTx Org31MSP
createAncorPeerTx Org32MSP
createAncorPeerTx Org33MSP
createAncorPeerTx Org34MSP
createAncorPeerTx Org35MSP
createAncorPeerTx Org36MSP
createAncorPeerTx Org37MSP
createAncorPeerTx Org38MSP
createAncorPeerTx Org39MSP
createAncorPeerTx Org40MSP
createAncorPeerTx Org41MSP
createAncorPeerTx Org42MSP
createAncorPeerTx Org43MSP
createAncorPeerTx Org44MSP
createAncorPeerTx Org45MSP
createAncorPeerTx Org46MSP
createAncorPeerTx Org47MSP
createAncorPeerTx Org48MSP
createAncorPeerTx Org49MSP
createAncorPeerTx Org50MSP
createAncorPeerTx Org51MSP
createAncorPeerTx Org52MSP
createAncorPeerTx Org53MSP
createAncorPeerTx Org54MSP
createAncorPeerTx Org55MSP
createAncorPeerTx Org56MSP
createAncorPeerTx Org57MSP
createAncorPeerTx Org58MSP
createAncorPeerTx Org59MSP
createAncorPeerTx Org60MSP
createAncorPeerTx Org61MSP
createAncorPeerTx Org62MSP
createAncorPeerTx Org63MSP
createAncorPeerTx Org64MSP
createAncorPeerTx Org65MSP
createAncorPeerTx Org66MSP
createAncorPeerTx Org67MSP
createAncorPeerTx Org68MSP
createAncorPeerTx Org69MSP
createAncorPeerTx Org70MSP
createAncorPeerTx Org71MSP
createAncorPeerTx Org72MSP
createAncorPeerTx Org73MSP
createAncorPeerTx Org74MSP
createAncorPeerTx Org75MSP
createAncorPeerTx Org76MSP
createAncorPeerTx Org77MSP
createAncorPeerTx Org78MSP
createAncorPeerTx Org79MSP
createAncorPeerTx Org80MSP
createAncorPeerTx Org81MSP
createAncorPeerTx Org82MSP
createAncorPeerTx Org83MSP
createAncorPeerTx Org84MSP
createAncorPeerTx Org85MSP
createAncorPeerTx Org86MSP
createAncorPeerTx Org87MSP
createAncorPeerTx Org88MSP
createAncorPeerTx Org89MSP
createAncorPeerTx Org90MSP
createAncorPeerTx Org91MSP
createAncorPeerTx Org92MSP
createAncorPeerTx Org93MSP
createAncorPeerTx Org94MSP
createAncorPeerTx Org95MSP
createAncorPeerTx Org96MSP
createAncorPeerTx Org97MSP
createAncorPeerTx Org98MSP
createAncorPeerTx Org99MSP
createAncorPeerTx Org100MSP

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
joinChannel 21
joinChannel 22
joinChannel 23
joinChannel 24
joinChannel 25
joinChannel 26
joinChannel 27
joinChannel 28
joinChannel 29
joinChannel 30
joinChannel 31
joinChannel 32
joinChannel 33
joinChannel 34
joinChannel 35
joinChannel 36
joinChannel 37
joinChannel 38
joinChannel 39
joinChannel 40
joinChannel 41
joinChannel 42
joinChannel 43
joinChannel 44
joinChannel 45
joinChannel 46
joinChannel 47
joinChannel 48
joinChannel 49
joinChannel 50
joinChannel 51
joinChannel 52
joinChannel 53
joinChannel 54
joinChannel 55
joinChannel 56
joinChannel 57
joinChannel 58
joinChannel 59
joinChannel 60
joinChannel 61
joinChannel 62
joinChannel 63
joinChannel 64
joinChannel 65
joinChannel 66
joinChannel 67
joinChannel 68
joinChannel 69
joinChannel 70
joinChannel 71
joinChannel 72
joinChannel 73
joinChannel 74
joinChannel 75
joinChannel 76
joinChannel 77
joinChannel 78
joinChannel 79
joinChannel 80
joinChannel 81
joinChannel 82
joinChannel 83
joinChannel 84
joinChannel 85
joinChannel 86
joinChannel 87
joinChannel 88
joinChannel 89
joinChannel 90
joinChannel 91
joinChannel 92
joinChannel 93
joinChannel 94
joinChannel 95
joinChannel 96
joinChannel 97
joinChannel 98
joinChannel 99
joinChannel 100

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
updateAnchorPeers 21
updateAnchorPeers 22
updateAnchorPeers 23
updateAnchorPeers 24
updateAnchorPeers 25
updateAnchorPeers 26
updateAnchorPeers 27
updateAnchorPeers 28
updateAnchorPeers 29
updateAnchorPeers 30
updateAnchorPeers 31
updateAnchorPeers 32
updateAnchorPeers 33
updateAnchorPeers 34
updateAnchorPeers 35
updateAnchorPeers 36
updateAnchorPeers 37
updateAnchorPeers 38
updateAnchorPeers 39
updateAnchorPeers 40
updateAnchorPeers 41
updateAnchorPeers 42
updateAnchorPeers 43
updateAnchorPeers 44
updateAnchorPeers 45
updateAnchorPeers 46
updateAnchorPeers 47
updateAnchorPeers 48
updateAnchorPeers 49
updateAnchorPeers 50
updateAnchorPeers 51
updateAnchorPeers 52
updateAnchorPeers 53
updateAnchorPeers 54
updateAnchorPeers 55
updateAnchorPeers 56
updateAnchorPeers 57
updateAnchorPeers 58
updateAnchorPeers 59
updateAnchorPeers 60
updateAnchorPeers 61
updateAnchorPeers 62
updateAnchorPeers 63
updateAnchorPeers 64
updateAnchorPeers 65
updateAnchorPeers 66
updateAnchorPeers 67
updateAnchorPeers 68
updateAnchorPeers 69
updateAnchorPeers 70
updateAnchorPeers 71
updateAnchorPeers 72
updateAnchorPeers 73
updateAnchorPeers 74
updateAnchorPeers 75
updateAnchorPeers 76
updateAnchorPeers 77
updateAnchorPeers 78
updateAnchorPeers 79
updateAnchorPeers 80
updateAnchorPeers 81
updateAnchorPeers 82
updateAnchorPeers 83
updateAnchorPeers 84
updateAnchorPeers 85
updateAnchorPeers 86
updateAnchorPeers 87
updateAnchorPeers 88
updateAnchorPeers 89
updateAnchorPeers 90
updateAnchorPeers 91
updateAnchorPeers 92
updateAnchorPeers 93
updateAnchorPeers 94
updateAnchorPeers 95
updateAnchorPeers 96
updateAnchorPeers 97
updateAnchorPeers 98
updateAnchorPeers 99
updateAnchorPeers 100

echo
echo "========= Channel successfully joined =========== "
echo

exit 0

