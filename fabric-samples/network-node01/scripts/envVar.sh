
Node01Addr=10.137.3.70
Node02Addr=10.137.3.71
Node03Addr=10.137.3.68
Node04Addr=10.137.3.20
Node05Addr=10.137.3.69
Node06Addr=10.137.3.6
Node07Addr=10.137.3.23
Node08Addr=10.137.3.90
Node09Addr=10.137.3.91
Node10Addr=10.137.3.88

# This is a collection of bash functions used by different scripts

export CORE_PEER_TLS_ENABLED=true
export ORDERER_CA=${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem
export PEER0_ORG1_CA=${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt
export PEER0_ORG2_CA=${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt
export PEER0_ORG3_CA=${PWD}/organizations/peerOrganizations/org3.example.com/peers/peer0.org3.example.com/tls/ca.crt
export PEER0_ORG4_CA=${PWD}/organizations/peerOrganizations/org4.example.com/peers/peer0.org4.example.com/tls/ca.crt
export PEER0_ORG5_CA=${PWD}/organizations/peerOrganizations/org5.example.com/peers/peer0.org5.example.com/tls/ca.crt
export PEER0_ORG6_CA=${PWD}/organizations/peerOrganizations/org6.example.com/peers/peer0.org6.example.com/tls/ca.crt
export PEER0_ORG7_CA=${PWD}/organizations/peerOrganizations/org7.example.com/peers/peer0.org7.example.com/tls/ca.crt
export PEER0_ORG8_CA=${PWD}/organizations/peerOrganizations/org8.example.com/peers/peer0.org8.example.com/tls/ca.crt
export PEER0_ORG9_CA=${PWD}/organizations/peerOrganizations/org9.example.com/peers/peer0.org9.example.com/tls/ca.crt
export PEER0_ORG10_CA=${PWD}/organizations/peerOrganizations/org10.example.com/peers/peer0.org10.example.com/tls/ca.crt
export PEER0_ORG11_CA=${PWD}/organizations/peerOrganizations/org11.example.com/peers/peer0.org11.example.com/tls/ca.crt
export PEER0_ORG12_CA=${PWD}/organizations/peerOrganizations/org12.example.com/peers/peer0.org12.example.com/tls/ca.crt
export PEER0_ORG13_CA=${PWD}/organizations/peerOrganizations/org13.example.com/peers/peer0.org13.example.com/tls/ca.crt
export PEER0_ORG14_CA=${PWD}/organizations/peerOrganizations/org14.example.com/peers/peer0.org14.example.com/tls/ca.crt
export PEER0_ORG15_CA=${PWD}/organizations/peerOrganizations/org15.example.com/peers/peer0.org15.example.com/tls/ca.crt
export PEER0_ORG16_CA=${PWD}/organizations/peerOrganizations/org16.example.com/peers/peer0.org16.example.com/tls/ca.crt
export PEER0_ORG17_CA=${PWD}/organizations/peerOrganizations/org17.example.com/peers/peer0.org17.example.com/tls/ca.crt
export PEER0_ORG18_CA=${PWD}/organizations/peerOrganizations/org18.example.com/peers/peer0.org18.example.com/tls/ca.crt
export PEER0_ORG19_CA=${PWD}/organizations/peerOrganizations/org19.example.com/peers/peer0.org19.example.com/tls/ca.crt
export PEER0_ORG20_CA=${PWD}/organizations/peerOrganizations/org20.example.com/peers/peer0.org20.example.com/tls/ca.crt
export PEER0_ORG21_CA=${PWD}/organizations/peerOrganizations/org21.example.com/peers/peer0.org21.example.com/tls/ca.crt
export PEER0_ORG22_CA=${PWD}/organizations/peerOrganizations/org22.example.com/peers/peer0.org22.example.com/tls/ca.crt
export PEER0_ORG23_CA=${PWD}/organizations/peerOrganizations/org23.example.com/peers/peer0.org23.example.com/tls/ca.crt
export PEER0_ORG24_CA=${PWD}/organizations/peerOrganizations/org24.example.com/peers/peer0.org24.example.com/tls/ca.crt
export PEER0_ORG25_CA=${PWD}/organizations/peerOrganizations/org25.example.com/peers/peer0.org25.example.com/tls/ca.crt
export PEER0_ORG26_CA=${PWD}/organizations/peerOrganizations/org26.example.com/peers/peer0.org26.example.com/tls/ca.crt
export PEER0_ORG27_CA=${PWD}/organizations/peerOrganizations/org27.example.com/peers/peer0.org27.example.com/tls/ca.crt
export PEER0_ORG28_CA=${PWD}/organizations/peerOrganizations/org28.example.com/peers/peer0.org28.example.com/tls/ca.crt
export PEER0_ORG29_CA=${PWD}/organizations/peerOrganizations/org29.example.com/peers/peer0.org29.example.com/tls/ca.crt
export PEER0_ORG30_CA=${PWD}/organizations/peerOrganizations/org30.example.com/peers/peer0.org30.example.com/tls/ca.crt

# Set OrdererOrg.Admin globals
setOrdererGlobals() {
  export CORE_PEER_LOCALMSPID="OrdererMSP"
  export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem
  export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/ordererOrganizations/example.com/users/Admin@example.com/msp
}

# Set environment variables for the peer org
setGlobals() {
  local USING_ORG=""
  if [ -z "$OVERRIDE_ORG" ]; then
    USING_ORG=$1
  else
    USING_ORG="${OVERRIDE_ORG}"
  fi
  echo "Using organization ${USING_ORG}"
  if [ $USING_ORG -eq 1 ]; then
    export CORE_PEER_LOCALMSPID="Org1MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG1_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp
    export CORE_PEER_ADDRESS=${Node01Addr}:7051
  elif [ $USING_ORG -eq 2 ]; then
    export CORE_PEER_LOCALMSPID="Org2MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG2_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org2.example.com/users/Admin@org2.example.com/msp
    export CORE_PEER_ADDRESS=${Node01Addr}:9051
  elif [ $USING_ORG -eq 3 ]; then
    export CORE_PEER_LOCALMSPID="Org3MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG3_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org3.example.com/users/Admin@org3.example.com/msp
    export CORE_PEER_ADDRESS=${Node01Addr}:10051
  elif [ $USING_ORG -eq 4 ]; then
    export CORE_PEER_LOCALMSPID="Org4MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG4_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org4.example.com/users/Admin@org4.example.com/msp
    export CORE_PEER_ADDRESS=${Node02Addr}:11051
  elif [ $USING_ORG -eq 5 ]; then
    export CORE_PEER_LOCALMSPID="Org5MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG5_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org5.example.com/users/Admin@org5.example.com/msp
    export CORE_PEER_ADDRESS=${Node02Addr}:12051
  elif [ $USING_ORG -eq 6 ]; then
    export CORE_PEER_LOCALMSPID="Org6MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG6_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org6.example.com/users/Admin@org6.example.com/msp
    export CORE_PEER_ADDRESS=${Node02Addr}:13051
  elif [ $USING_ORG -eq 7 ]; then
    export CORE_PEER_LOCALMSPID="Org7MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG7_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org7.example.com/users/Admin@org7.example.com/msp
    export CORE_PEER_ADDRESS=${Node03Addr}:14051
  elif [ $USING_ORG -eq 8 ]; then
    export CORE_PEER_LOCALMSPID="Org8MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG8_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org8.example.com/users/Admin@org8.example.com/msp
    export CORE_PEER_ADDRESS=${Node03Addr}:15051
  elif [ $USING_ORG -eq 9 ]; then
    export CORE_PEER_LOCALMSPID="Org9MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG9_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org9.example.com/users/Admin@org9.example.com/msp
    export CORE_PEER_ADDRESS=${Node03Addr}:16051
  elif [ $USING_ORG -eq 10 ]; then
    export CORE_PEER_LOCALMSPID="Org10MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG10_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org10.example.com/users/Admin@org10.example.com/msp
    export CORE_PEER_ADDRESS=${Node04Addr}:17051
  elif [ $USING_ORG -eq 11 ]; then
    export CORE_PEER_LOCALMSPID="Org11MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG11_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org11.example.com/users/Admin@org11.example.com/msp
    export CORE_PEER_ADDRESS=${Node04Addr}:7051
  elif [ $USING_ORG -eq 12 ]; then
    export CORE_PEER_LOCALMSPID="Org12MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG12_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org12.example.com/users/Admin@org12.example.com/msp
    export CORE_PEER_ADDRESS=${Node04Addr}:9051
  elif [ $USING_ORG -eq 13 ]; then
    export CORE_PEER_LOCALMSPID="Org13MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG13_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org13.example.com/users/Admin@org13.example.com/msp
    export CORE_PEER_ADDRESS=${Node05Addr}:10051
  elif [ $USING_ORG -eq 14 ]; then
    export CORE_PEER_LOCALMSPID="Org14MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG14_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org14.example.com/users/Admin@org14.example.com/msp
    export CORE_PEER_ADDRESS=${Node05Addr}:11051
  elif [ $USING_ORG -eq 15 ]; then
    export CORE_PEER_LOCALMSPID="Org15MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG15_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org15.example.com/users/Admin@org15.example.com/msp
    export CORE_PEER_ADDRESS=${Node05Addr}:12051
  elif [ $USING_ORG -eq 16 ]; then
    export CORE_PEER_LOCALMSPID="Org16MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG16_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org16.example.com/users/Admin@org16.example.com/msp
    export CORE_PEER_ADDRESS=${Node06Addr}:13051
  elif [ $USING_ORG -eq 17 ]; then
    export CORE_PEER_LOCALMSPID="Org17MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG17_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org17.example.com/users/Admin@org17.example.com/msp
    export CORE_PEER_ADDRESS=${Node06Addr}:14051
  elif [ $USING_ORG -eq 18 ]; then
    export CORE_PEER_LOCALMSPID="Org18MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG18_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org18.example.com/users/Admin@org18.example.com/msp
    export CORE_PEER_ADDRESS=${Node06Addr}:15051
  elif [ $USING_ORG -eq 19 ]; then
    export CORE_PEER_LOCALMSPID="Org19MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG19_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org19.example.com/users/Admin@org19.example.com/msp
    export CORE_PEER_ADDRESS=${Node07Addr}:16051
  elif [ $USING_ORG -eq 20 ]; then
    export CORE_PEER_LOCALMSPID="Org20MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG20_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org20.example.com/users/Admin@org20.example.com/msp
    export CORE_PEER_ADDRESS=${Node07Addr}:17051
  elif [ $USING_ORG -eq 21 ]; then
    export CORE_PEER_LOCALMSPID="Org21MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG21_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org21.example.com/users/Admin@org21.example.com/msp
    export CORE_PEER_ADDRESS=${Node07Addr}:7051
  elif [ $USING_ORG -eq 22 ]; then
    export CORE_PEER_LOCALMSPID="Org22MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG22_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org22.example.com/users/Admin@org22.example.com/msp
    export CORE_PEER_ADDRESS=${Node08Addr}:9051
  elif [ $USING_ORG -eq 23 ]; then
    export CORE_PEER_LOCALMSPID="Org23MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG23_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org23.example.com/users/Admin@org23.example.com/msp
    export CORE_PEER_ADDRESS=${Node08Addr}:10051
  elif [ $USING_ORG -eq 24 ]; then
    export CORE_PEER_LOCALMSPID="Org24MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG24_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org24.example.com/users/Admin@org24.example.com/msp
    export CORE_PEER_ADDRESS=${Node08Addr}:11051
  elif [ $USING_ORG -eq 25 ]; then
    export CORE_PEER_LOCALMSPID="Org25MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG25_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org25.example.com/users/Admin@org25.example.com/msp
    export CORE_PEER_ADDRESS=${Node09Addr}:12051
  elif [ $USING_ORG -eq 26 ]; then
    export CORE_PEER_LOCALMSPID="Org26MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG26_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org26.example.com/users/Admin@org26.example.com/msp
    export CORE_PEER_ADDRESS=${Node09Addr}:13051
  elif [ $USING_ORG -eq 27 ]; then
    export CORE_PEER_LOCALMSPID="Org27MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG27_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org27.example.com/users/Admin@org27.example.com/msp
    export CORE_PEER_ADDRESS=${Node09Addr}:14051
  elif [ $USING_ORG -eq 28 ]; then
    export CORE_PEER_LOCALMSPID="Org28MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG28_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org28.example.com/users/Admin@org28.example.com/msp
    export CORE_PEER_ADDRESS=${Node10Addr}:15051
  elif [ $USING_ORG -eq 29 ]; then
    export CORE_PEER_LOCALMSPID="Org29MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG29_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org29.example.com/users/Admin@org29.example.com/msp
    export CORE_PEER_ADDRESS=${Node10Addr}:16051
  elif [ $USING_ORG -eq 30 ]; then
    export CORE_PEER_LOCALMSPID="Org30MSP"
    export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG30_CA
    export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org30.example.com/users/Admin@org30.example.com/msp
    export CORE_PEER_ADDRESS=${Node10Addr}:17051
  else
    echo "================== ERROR !!! ORG Unknown =================="
  fi

  if [ "$VERBOSE" == "true" ]; then
    env | grep CORE
  fi
}

# parsePeerConnectionParameters $@
# Helper function that sets the peer connection parameters for a chaincode
# operation
parsePeerConnectionParameters() {

  PEER_CONN_PARMS=""
  PEERS=""
  while [ "$#" -gt 0 ]; do
    setGlobals $1
    PEER="peer0.org$1"
    ## Set peer adresses
    PEERS="$PEERS $PEER"
    PEER_CONN_PARMS="$PEER_CONN_PARMS --peerAddresses $CORE_PEER_ADDRESS"
    ## Set path to TLS certificate
    TLSINFO=$(eval echo "--tlsRootCertFiles \$PEER0_ORG$1_CA")
    PEER_CONN_PARMS="$PEER_CONN_PARMS $TLSINFO"
    # shift by one to get to the next organization
    shift
  done
  # remove leading space for output
  PEERS="$(echo -e "$PEERS" | sed -e 's/^[[:space:]]*//')"
}

verifyResult() {
  if [ $1 -ne 0 ]; then
    echo "!!!!!!!!!!!!!!! "$2" !!!!!!!!!!!!!!!!"
    echo
    exit 1
  fi
}

