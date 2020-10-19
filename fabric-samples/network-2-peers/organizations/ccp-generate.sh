#!/bin/bash

function one_line_pem {
    echo "`awk 'NF {sub(/\\n/, ""); printf "%s\\\\\\\n",$0;}' $1`"
}

function json_ccp {
    local PP=$(one_line_pem $5)
    local CP=$(one_line_pem $6)
    sed -e "s/\${ORG}/$1/" \
        -e "s/\${P0IPADDR}/$2/" \
        -e "s/\${P0PORT}/$3/" \
        -e "s/\${CAPORT}/$4/" \
        -e "s#\${PEERPEM}#$PP#" \
        -e "s#\${CAPEM}#$CP#" \
        organizations/ccp-template.json
}

# envrionments setting below

ORG1=1
ORG2=2


P0IPADDRORG1=localhost
P0IPADDRORG2=localhost

P0PORTORG1=7051
P0PORTORG2=9051

CAPORTORG1=7054
CAPORTORG2=9054

PEERPEMORG1=organizations/peerOrganizations/org1.example.com/tlsca/tlsca.org1.example.com-cert.pem
PEERPEMORG2=organizations/peerOrganizations/org2.example.com/tlsca/tlsca.org2.example.com-cert.pem

CAPEMORG1=organizations/peerOrganizations/org1.example.com/ca/ca.org1.example.com-cert.pem
CAPEMORG2=organizations/peerOrganizations/org2.example.com/ca/ca.org2.example.com-cert.pem


echo "$(json_ccp $ORG1 $P0IPADDRORG1 $P0PORTORG1 $CAPORTORG1 $PEERPEMORG1 $CAPEMORG1)" > organizations/peerOrganizations/org1.example.com/connection-org1.json
echo "$(json_ccp $ORG2 $P0IPADDRORG2 $P0PORTORG2 $CAPORTORG2 $PEERPEMORG2 $CAPEMORG2)" > organizations/peerOrganizations/org2.example.com/connection-org2.json

