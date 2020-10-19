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
ORG3=3
ORG4=4
ORG5=5
ORG6=6
ORG7=7
ORG8=8
ORG9=9
ORG10=10


P0IPADDRORG1=10.137.3.70
P0IPADDRORG2=10.137.3.71
P0IPADDRORG3=10.137.3.68
P0IPADDRORG4=10.137.3.20
P0IPADDRORG5=10.137.3.69
P0IPADDRORG6=10.137.3.6
P0IPADDRORG7=10.137.3.23
P0IPADDRORG8=10.137.3.90
P0IPADDRORG9=10.137.3.91
P0IPADDRORG10=10.137.3.88

P0PORTORG1=7051
P0PORTORG2=9051
P0PORTORG3=10051
P0PORTORG4=11051
P0PORTORG5=12051
P0PORTORG6=13051
P0PORTORG7=14051
P0PORTORG8=15051
P0PORTORG9=16051
P0PORTORG10=17051

CAPORTORG1=7054
CAPORTORG2=7054
CAPORTORG3=7054
CAPORTORG4=7054
CAPORTORG5=7054
CAPORTORG6=7054
CAPORTORG7=7054
CAPORTORG8=7054
CAPORTORG9=7054
CAPORTORG10=7054

PEERPEMORG1=organizations/peerOrganizations/org1.example.com/tlsca/tlsca.org1.example.com-cert.pem
PEERPEMORG2=organizations/peerOrganizations/org2.example.com/tlsca/tlsca.org2.example.com-cert.pem
PEERPEMORG3=organizations/peerOrganizations/org3.example.com/tlsca/tlsca.org3.example.com-cert.pem
PEERPEMORG4=organizations/peerOrganizations/org4.example.com/tlsca/tlsca.org4.example.com-cert.pem
PEERPEMORG5=organizations/peerOrganizations/org5.example.com/tlsca/tlsca.org5.example.com-cert.pem
PEERPEMORG6=organizations/peerOrganizations/org6.example.com/tlsca/tlsca.org6.example.com-cert.pem
PEERPEMORG7=organizations/peerOrganizations/org7.example.com/tlsca/tlsca.org7.example.com-cert.pem
PEERPEMORG8=organizations/peerOrganizations/org8.example.com/tlsca/tlsca.org8.example.com-cert.pem
PEERPEMORG9=organizations/peerOrganizations/org9.example.com/tlsca/tlsca.org9.example.com-cert.pem
PEERPEMORG10=organizations/peerOrganizations/org10.example.com/tlsca/tlsca.org10.example.com-cert.pem

CAPEMORG1=organizations/peerOrganizations/org1.example.com/ca/ca.org1.example.com-cert.pem
CAPEMORG2=organizations/peerOrganizations/org2.example.com/ca/ca.org2.example.com-cert.pem
CAPEMORG3=organizations/peerOrganizations/org3.example.com/ca/ca.org3.example.com-cert.pem
CAPEMORG4=organizations/peerOrganizations/org4.example.com/ca/ca.org4.example.com-cert.pem
CAPEMORG5=organizations/peerOrganizations/org5.example.com/ca/ca.org5.example.com-cert.pem
CAPEMORG6=organizations/peerOrganizations/org6.example.com/ca/ca.org6.example.com-cert.pem
CAPEMORG7=organizations/peerOrganizations/org7.example.com/ca/ca.org7.example.com-cert.pem
CAPEMORG8=organizations/peerOrganizations/org8.example.com/ca/ca.org8.example.com-cert.pem
CAPEMORG9=organizations/peerOrganizations/org9.example.com/ca/ca.org9.example.com-cert.pem
CAPEMORG10=organizations/peerOrganizations/org10.example.com/ca/ca.org10.example.com-cert.pem


echo "$(json_ccp $ORG1 $P0IPADDRORG1 $P0PORTORG1 $CAPORTORG1 $PEERPEMORG1 $CAPEMORG1)" > organizations/peerOrganizations/org1.example.com/connection-org1.json
echo "$(json_ccp $ORG2 $P0IPADDRORG2 $P0PORTORG2 $CAPORTORG2 $PEERPEMORG2 $CAPEMORG2)" > organizations/peerOrganizations/org2.example.com/connection-org2.json
echo "$(json_ccp $ORG3 $P0IPADDRORG3 $P0PORTORG3 $CAPORTORG3 $PEERPEMORG3 $CAPEMORG3)" > organizations/peerOrganizations/org3.example.com/connection-org3.json
echo "$(json_ccp $ORG4 $P0IPADDRORG4 $P0PORTORG4 $CAPORTORG4 $PEERPEMORG4 $CAPEMORG4)" > organizations/peerOrganizations/org4.example.com/connection-org4.json
echo "$(json_ccp $ORG5 $P0IPADDRORG5 $P0PORTORG5 $CAPORTORG5 $PEERPEMORG5 $CAPEMORG5)" > organizations/peerOrganizations/org5.example.com/connection-org5.json
echo "$(json_ccp $ORG6 $P0IPADDRORG6 $P0PORTORG6 $CAPORTORG6 $PEERPEMORG6 $CAPEMORG6)" > organizations/peerOrganizations/org6.example.com/connection-org6.json
echo "$(json_ccp $ORG7 $P0IPADDRORG7 $P0PORTORG7 $CAPORTORG7 $PEERPEMORG7 $CAPEMORG7)" > organizations/peerOrganizations/org7.example.com/connection-org7.json
echo "$(json_ccp $ORG8 $P0IPADDRORG8 $P0PORTORG8 $CAPORTORG8 $PEERPEMORG8 $CAPEMORG8)" > organizations/peerOrganizations/org8.example.com/connection-org8.json
echo "$(json_ccp $ORG9 $P0IPADDRORG9 $P0PORTORG9 $CAPORTORG9 $PEERPEMORG9 $CAPEMORG9)" > organizations/peerOrganizations/org9.example.com/connection-org9.json
echo "$(json_ccp $ORG10 $P0IPADDRORG10 $P0PORTORG10 $CAPORTORG10 $PEERPEMORG10 $CAPEMORG10)" > organizations/peerOrganizations/org10.example.com/connection-org10.json
