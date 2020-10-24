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
ORG11=11
ORG12=12
ORG13=13
ORG14=14
ORG15=15
ORG16=16
ORG17=17
ORG18=18
ORG19=19
ORG20=20
ORG21=21
ORG22=22
ORG23=23
ORG24=24
ORG25=25
ORG26=26
ORG27=27
ORG28=28
ORG29=29
ORG30=30
ORG31=31
ORG32=32
ORG33=33
ORG34=34
ORG35=35
ORG36=36
ORG37=37
ORG38=38
ORG39=39
ORG40=40
ORG41=41
ORG42=42
ORG43=43
ORG44=44
ORG45=45
ORG46=46
ORG47=47
ORG48=48
ORG49=49
ORG50=50

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

P0IPADDRORG1=${Node01Addr}
P0IPADDRORG2=${Node01Addr}
P0IPADDRORG3=${Node01Addr}
P0IPADDRORG4=${Node01Addr}
P0IPADDRORG5=${Node01Addr}
P0IPADDRORG6=${Node02Addr}
P0IPADDRORG7=${Node02Addr}
P0IPADDRORG8=${Node02Addr}
P0IPADDRORG9=${Node02Addr}
P0IPADDRORG10=${Node02Addr}
P0IPADDRORG11=${Node03Addr}
P0IPADDRORG12=${Node03Addr}
P0IPADDRORG13=${Node03Addr}
P0IPADDRORG14=${Node03Addr}
P0IPADDRORG15=${Node03Addr}
P0IPADDRORG16=${Node04Addr}
P0IPADDRORG17=${Node04Addr}
P0IPADDRORG18=${Node04Addr}
P0IPADDRORG19=${Node04Addr}
P0IPADDRORG20=${Node04Addr}
P0IPADDRORG21=${Node05Addr}
P0IPADDRORG22=${Node05Addr}
P0IPADDRORG23=${Node05Addr}
P0IPADDRORG24=${Node05Addr}
P0IPADDRORG25=${Node05Addr}
P0IPADDRORG26=${Node06Addr}
P0IPADDRORG27=${Node06Addr}
P0IPADDRORG28=${Node06Addr}
P0IPADDRORG29=${Node06Addr}
P0IPADDRORG30=${Node06Addr}
P0IPADDRORG31=${Node07Addr}
P0IPADDRORG32=${Node07Addr}
P0IPADDRORG33=${Node07Addr}
P0IPADDRORG34=${Node07Addr}
P0IPADDRORG35=${Node07Addr}
P0IPADDRORG36=${Node08Addr}
P0IPADDRORG37=${Node08Addr}
P0IPADDRORG38=${Node08Addr}
P0IPADDRORG39=${Node08Addr}
P0IPADDRORG40=${Node08Addr}
P0IPADDRORG41=${Node09Addr}
P0IPADDRORG42=${Node09Addr}
P0IPADDRORG43=${Node09Addr}
P0IPADDRORG44=${Node09Addr}
P0IPADDRORG45=${Node09Addr}
P0IPADDRORG46=${Node10Addr}
P0IPADDRORG47=${Node10Addr}
P0IPADDRORG48=${Node10Addr}
P0IPADDRORG49=${Node10Addr}
P0IPADDRORG50=${Node10Addr}

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
P0PORTORG11=7051
P0PORTORG12=9051
P0PORTORG13=10051
P0PORTORG14=11051
P0PORTORG15=12051
P0PORTORG16=13051
P0PORTORG17=14051
P0PORTORG18=15051
P0PORTORG19=16051
P0PORTORG20=17051
P0PORTORG21=7051
P0PORTORG22=9051
P0PORTORG23=10051
P0PORTORG24=11051
P0PORTORG25=12051
P0PORTORG26=13051
P0PORTORG27=14051
P0PORTORG28=15051
P0PORTORG29=16051
P0PORTORG30=17051
P0PORTORG31=7051
P0PORTORG32=9051
P0PORTORG33=10051
P0PORTORG34=11051
P0PORTORG35=12051
P0PORTORG36=13051
P0PORTORG37=14051
P0PORTORG38=15051
P0PORTORG39=16051
P0PORTORG40=17051
P0PORTORG41=7051
P0PORTORG42=9051
P0PORTORG43=10051
P0PORTORG44=11051
P0PORTORG45=12051
P0PORTORG46=13051
P0PORTORG47=14051
P0PORTORG48=15051
P0PORTORG49=16051
P0PORTORG50=17051

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
CAPORTORG11=7054
CAPORTORG12=7054
CAPORTORG13=7054
CAPORTORG14=7054
CAPORTORG15=7054
CAPORTORG16=7054
CAPORTORG17=7054
CAPORTORG18=7054
CAPORTORG19=7054
CAPORTORG20=7054
CAPORTORG21=7054
CAPORTORG22=7054
CAPORTORG23=7054
CAPORTORG24=7054
CAPORTORG25=7054
CAPORTORG26=7054
CAPORTORG27=7054
CAPORTORG28=7054
CAPORTORG29=7054
CAPORTORG30=7054
CAPORTORG31=7054
CAPORTORG32=7054
CAPORTORG33=7054
CAPORTORG34=7054
CAPORTORG35=7054
CAPORTORG36=7054
CAPORTORG37=7054
CAPORTORG38=7054
CAPORTORG39=7054
CAPORTORG40=7054
CAPORTORG41=7054
CAPORTORG42=7054
CAPORTORG43=7054
CAPORTORG44=7054
CAPORTORG45=7054
CAPORTORG46=7054
CAPORTORG47=7054
CAPORTORG48=7054
CAPORTORG49=7054
CAPORTORG50=7054

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
PEERPEMORG11=organizations/peerOrganizations/org11.example.com/tlsca/tlsca.org11.example.com-cert.pem
PEERPEMORG12=organizations/peerOrganizations/org12.example.com/tlsca/tlsca.org12.example.com-cert.pem
PEERPEMORG13=organizations/peerOrganizations/org13.example.com/tlsca/tlsca.org13.example.com-cert.pem
PEERPEMORG14=organizations/peerOrganizations/org14.example.com/tlsca/tlsca.org14.example.com-cert.pem
PEERPEMORG15=organizations/peerOrganizations/org15.example.com/tlsca/tlsca.org15.example.com-cert.pem
PEERPEMORG16=organizations/peerOrganizations/org16.example.com/tlsca/tlsca.org16.example.com-cert.pem
PEERPEMORG17=organizations/peerOrganizations/org17.example.com/tlsca/tlsca.org17.example.com-cert.pem
PEERPEMORG18=organizations/peerOrganizations/org18.example.com/tlsca/tlsca.org18.example.com-cert.pem
PEERPEMORG19=organizations/peerOrganizations/org19.example.com/tlsca/tlsca.org19.example.com-cert.pem
PEERPEMORG20=organizations/peerOrganizations/org20.example.com/tlsca/tlsca.org20.example.com-cert.pem
PEERPEMORG21=organizations/peerOrganizations/org21.example.com/tlsca/tlsca.org21.example.com-cert.pem
PEERPEMORG22=organizations/peerOrganizations/org22.example.com/tlsca/tlsca.org22.example.com-cert.pem
PEERPEMORG23=organizations/peerOrganizations/org23.example.com/tlsca/tlsca.org23.example.com-cert.pem
PEERPEMORG24=organizations/peerOrganizations/org24.example.com/tlsca/tlsca.org24.example.com-cert.pem
PEERPEMORG25=organizations/peerOrganizations/org25.example.com/tlsca/tlsca.org25.example.com-cert.pem
PEERPEMORG26=organizations/peerOrganizations/org26.example.com/tlsca/tlsca.org26.example.com-cert.pem
PEERPEMORG27=organizations/peerOrganizations/org27.example.com/tlsca/tlsca.org27.example.com-cert.pem
PEERPEMORG28=organizations/peerOrganizations/org28.example.com/tlsca/tlsca.org28.example.com-cert.pem
PEERPEMORG29=organizations/peerOrganizations/org29.example.com/tlsca/tlsca.org29.example.com-cert.pem
PEERPEMORG30=organizations/peerOrganizations/org30.example.com/tlsca/tlsca.org30.example.com-cert.pem
PEERPEMORG31=organizations/peerOrganizations/org31.example.com/tlsca/tlsca.org31.example.com-cert.pem
PEERPEMORG32=organizations/peerOrganizations/org32.example.com/tlsca/tlsca.org32.example.com-cert.pem
PEERPEMORG33=organizations/peerOrganizations/org33.example.com/tlsca/tlsca.org33.example.com-cert.pem
PEERPEMORG34=organizations/peerOrganizations/org34.example.com/tlsca/tlsca.org34.example.com-cert.pem
PEERPEMORG35=organizations/peerOrganizations/org35.example.com/tlsca/tlsca.org35.example.com-cert.pem
PEERPEMORG36=organizations/peerOrganizations/org36.example.com/tlsca/tlsca.org36.example.com-cert.pem
PEERPEMORG37=organizations/peerOrganizations/org37.example.com/tlsca/tlsca.org37.example.com-cert.pem
PEERPEMORG38=organizations/peerOrganizations/org38.example.com/tlsca/tlsca.org38.example.com-cert.pem
PEERPEMORG39=organizations/peerOrganizations/org39.example.com/tlsca/tlsca.org39.example.com-cert.pem
PEERPEMORG40=organizations/peerOrganizations/org40.example.com/tlsca/tlsca.org40.example.com-cert.pem
PEERPEMORG41=organizations/peerOrganizations/org41.example.com/tlsca/tlsca.org41.example.com-cert.pem
PEERPEMORG42=organizations/peerOrganizations/org42.example.com/tlsca/tlsca.org42.example.com-cert.pem
PEERPEMORG43=organizations/peerOrganizations/org43.example.com/tlsca/tlsca.org43.example.com-cert.pem
PEERPEMORG44=organizations/peerOrganizations/org44.example.com/tlsca/tlsca.org44.example.com-cert.pem
PEERPEMORG45=organizations/peerOrganizations/org45.example.com/tlsca/tlsca.org45.example.com-cert.pem
PEERPEMORG46=organizations/peerOrganizations/org46.example.com/tlsca/tlsca.org46.example.com-cert.pem
PEERPEMORG47=organizations/peerOrganizations/org47.example.com/tlsca/tlsca.org47.example.com-cert.pem
PEERPEMORG48=organizations/peerOrganizations/org48.example.com/tlsca/tlsca.org48.example.com-cert.pem
PEERPEMORG49=organizations/peerOrganizations/org49.example.com/tlsca/tlsca.org49.example.com-cert.pem
PEERPEMORG50=organizations/peerOrganizations/org50.example.com/tlsca/tlsca.org50.example.com-cert.pem


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
CAPEMORG11=organizations/peerOrganizations/org11.example.com/ca/ca.org11.example.com-cert.pem
CAPEMORG12=organizations/peerOrganizations/org12.example.com/ca/ca.org12.example.com-cert.pem
CAPEMORG13=organizations/peerOrganizations/org13.example.com/ca/ca.org13.example.com-cert.pem
CAPEMORG14=organizations/peerOrganizations/org14.example.com/ca/ca.org14.example.com-cert.pem
CAPEMORG15=organizations/peerOrganizations/org15.example.com/ca/ca.org15.example.com-cert.pem
CAPEMORG16=organizations/peerOrganizations/org16.example.com/ca/ca.org16.example.com-cert.pem
CAPEMORG17=organizations/peerOrganizations/org17.example.com/ca/ca.org17.example.com-cert.pem
CAPEMORG18=organizations/peerOrganizations/org18.example.com/ca/ca.org18.example.com-cert.pem
CAPEMORG19=organizations/peerOrganizations/org19.example.com/ca/ca.org19.example.com-cert.pem
CAPEMORG20=organizations/peerOrganizations/org20.example.com/ca/ca.org20.example.com-cert.pem
CAPEMORG21=organizations/peerOrganizations/org21.example.com/ca/ca.org21.example.com-cert.pem
CAPEMORG22=organizations/peerOrganizations/org22.example.com/ca/ca.org22.example.com-cert.pem
CAPEMORG23=organizations/peerOrganizations/org23.example.com/ca/ca.org23.example.com-cert.pem
CAPEMORG24=organizations/peerOrganizations/org24.example.com/ca/ca.org24.example.com-cert.pem
CAPEMORG25=organizations/peerOrganizations/org25.example.com/ca/ca.org25.example.com-cert.pem
CAPEMORG26=organizations/peerOrganizations/org26.example.com/ca/ca.org26.example.com-cert.pem
CAPEMORG27=organizations/peerOrganizations/org27.example.com/ca/ca.org27.example.com-cert.pem
CAPEMORG28=organizations/peerOrganizations/org28.example.com/ca/ca.org28.example.com-cert.pem
CAPEMORG29=organizations/peerOrganizations/org29.example.com/ca/ca.org29.example.com-cert.pem
CAPEMORG30=organizations/peerOrganizations/org30.example.com/ca/ca.org30.example.com-cert.pem
CAPEMORG31=organizations/peerOrganizations/org31.example.com/ca/ca.org31.example.com-cert.pem
CAPEMORG32=organizations/peerOrganizations/org32.example.com/ca/ca.org32.example.com-cert.pem
CAPEMORG33=organizations/peerOrganizations/org33.example.com/ca/ca.org33.example.com-cert.pem
CAPEMORG34=organizations/peerOrganizations/org34.example.com/ca/ca.org34.example.com-cert.pem
CAPEMORG35=organizations/peerOrganizations/org35.example.com/ca/ca.org35.example.com-cert.pem
CAPEMORG36=organizations/peerOrganizations/org36.example.com/ca/ca.org36.example.com-cert.pem
CAPEMORG37=organizations/peerOrganizations/org37.example.com/ca/ca.org37.example.com-cert.pem
CAPEMORG38=organizations/peerOrganizations/org38.example.com/ca/ca.org38.example.com-cert.pem
CAPEMORG39=organizations/peerOrganizations/org39.example.com/ca/ca.org39.example.com-cert.pem
CAPEMORG40=organizations/peerOrganizations/org40.example.com/ca/ca.org40.example.com-cert.pem
CAPEMORG41=organizations/peerOrganizations/org41.example.com/ca/ca.org41.example.com-cert.pem
CAPEMORG42=organizations/peerOrganizations/org42.example.com/ca/ca.org42.example.com-cert.pem
CAPEMORG43=organizations/peerOrganizations/org43.example.com/ca/ca.org43.example.com-cert.pem
CAPEMORG44=organizations/peerOrganizations/org44.example.com/ca/ca.org44.example.com-cert.pem
CAPEMORG45=organizations/peerOrganizations/org45.example.com/ca/ca.org45.example.com-cert.pem
CAPEMORG46=organizations/peerOrganizations/org46.example.com/ca/ca.org46.example.com-cert.pem
CAPEMORG47=organizations/peerOrganizations/org47.example.com/ca/ca.org47.example.com-cert.pem
CAPEMORG48=organizations/peerOrganizations/org48.example.com/ca/ca.org48.example.com-cert.pem
CAPEMORG49=organizations/peerOrganizations/org49.example.com/ca/ca.org49.example.com-cert.pem
CAPEMORG50=organizations/peerOrganizations/org50.example.com/ca/ca.org50.example.com-cert.pem


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
echo "$(json_ccp $ORG11 $P0IPADDRORG11 $P0PORTORG11 $CAPORTORG11 $PEERPEMORG11 $CAPEMORG11)" > organizations/peerOrganizations/org11.example.com/connection-org11.json
echo "$(json_ccp $ORG12 $P0IPADDRORG12 $P0PORTORG12 $CAPORTORG12 $PEERPEMORG12 $CAPEMORG12)" > organizations/peerOrganizations/org12.example.com/connection-org12.json
echo "$(json_ccp $ORG13 $P0IPADDRORG13 $P0PORTORG13 $CAPORTORG13 $PEERPEMORG13 $CAPEMORG13)" > organizations/peerOrganizations/org13.example.com/connection-org13.json
echo "$(json_ccp $ORG14 $P0IPADDRORG14 $P0PORTORG14 $CAPORTORG14 $PEERPEMORG14 $CAPEMORG14)" > organizations/peerOrganizations/org14.example.com/connection-org14.json
echo "$(json_ccp $ORG15 $P0IPADDRORG15 $P0PORTORG15 $CAPORTORG15 $PEERPEMORG15 $CAPEMORG15)" > organizations/peerOrganizations/org15.example.com/connection-org15.json
echo "$(json_ccp $ORG16 $P0IPADDRORG16 $P0PORTORG16 $CAPORTORG16 $PEERPEMORG16 $CAPEMORG16)" > organizations/peerOrganizations/org16.example.com/connection-org16.json
echo "$(json_ccp $ORG17 $P0IPADDRORG17 $P0PORTORG17 $CAPORTORG17 $PEERPEMORG17 $CAPEMORG17)" > organizations/peerOrganizations/org17.example.com/connection-org17.json
echo "$(json_ccp $ORG18 $P0IPADDRORG18 $P0PORTORG18 $CAPORTORG18 $PEERPEMORG18 $CAPEMORG18)" > organizations/peerOrganizations/org18.example.com/connection-org18.json
echo "$(json_ccp $ORG19 $P0IPADDRORG19 $P0PORTORG19 $CAPORTORG19 $PEERPEMORG19 $CAPEMORG19)" > organizations/peerOrganizations/org19.example.com/connection-org19.json
echo "$(json_ccp $ORG20 $P0IPADDRORG20 $P0PORTORG20 $CAPORTORG20 $PEERPEMORG20 $CAPEMORG20)" > organizations/peerOrganizations/org20.example.com/connection-org20.json
echo "$(json_ccp $ORG21 $P0IPADDRORG21 $P0PORTORG21 $CAPORTORG21 $PEERPEMORG21 $CAPEMORG21)" > organizations/peerOrganizations/org21.example.com/connection-org21.json
echo "$(json_ccp $ORG22 $P0IPADDRORG22 $P0PORTORG22 $CAPORTORG22 $PEERPEMORG22 $CAPEMORG22)" > organizations/peerOrganizations/org22.example.com/connection-org22.json
echo "$(json_ccp $ORG23 $P0IPADDRORG23 $P0PORTORG23 $CAPORTORG23 $PEERPEMORG23 $CAPEMORG23)" > organizations/peerOrganizations/org23.example.com/connection-org23.json
echo "$(json_ccp $ORG24 $P0IPADDRORG24 $P0PORTORG24 $CAPORTORG24 $PEERPEMORG24 $CAPEMORG24)" > organizations/peerOrganizations/org24.example.com/connection-org24.json
echo "$(json_ccp $ORG25 $P0IPADDRORG25 $P0PORTORG25 $CAPORTORG25 $PEERPEMORG25 $CAPEMORG25)" > organizations/peerOrganizations/org25.example.com/connection-org25.json
echo "$(json_ccp $ORG26 $P0IPADDRORG26 $P0PORTORG26 $CAPORTORG26 $PEERPEMORG26 $CAPEMORG26)" > organizations/peerOrganizations/org26.example.com/connection-org26.json
echo "$(json_ccp $ORG27 $P0IPADDRORG27 $P0PORTORG27 $CAPORTORG27 $PEERPEMORG27 $CAPEMORG27)" > organizations/peerOrganizations/org27.example.com/connection-org27.json
echo "$(json_ccp $ORG28 $P0IPADDRORG28 $P0PORTORG28 $CAPORTORG28 $PEERPEMORG28 $CAPEMORG28)" > organizations/peerOrganizations/org28.example.com/connection-org28.json
echo "$(json_ccp $ORG29 $P0IPADDRORG29 $P0PORTORG29 $CAPORTORG29 $PEERPEMORG29 $CAPEMORG29)" > organizations/peerOrganizations/org29.example.com/connection-org29.json
echo "$(json_ccp $ORG30 $P0IPADDRORG30 $P0PORTORG30 $CAPORTORG30 $PEERPEMORG30 $CAPEMORG30)" > organizations/peerOrganizations/org30.example.com/connection-org30.json
echo "$(json_ccp $ORG31 $P0IPADDRORG31 $P0PORTORG31 $CAPORTORG31 $PEERPEMORG31 $CAPEMORG31)" > organizations/peerOrganizations/org31.example.com/connection-org31.json
echo "$(json_ccp $ORG32 $P0IPADDRORG32 $P0PORTORG32 $CAPORTORG32 $PEERPEMORG32 $CAPEMORG32)" > organizations/peerOrganizations/org32.example.com/connection-org32.json
echo "$(json_ccp $ORG33 $P0IPADDRORG33 $P0PORTORG33 $CAPORTORG33 $PEERPEMORG33 $CAPEMORG33)" > organizations/peerOrganizations/org33.example.com/connection-org33.json
echo "$(json_ccp $ORG34 $P0IPADDRORG34 $P0PORTORG34 $CAPORTORG34 $PEERPEMORG34 $CAPEMORG34)" > organizations/peerOrganizations/org34.example.com/connection-org34.json
echo "$(json_ccp $ORG35 $P0IPADDRORG35 $P0PORTORG35 $CAPORTORG35 $PEERPEMORG35 $CAPEMORG35)" > organizations/peerOrganizations/org35.example.com/connection-org35.json
echo "$(json_ccp $ORG36 $P0IPADDRORG36 $P0PORTORG36 $CAPORTORG36 $PEERPEMORG36 $CAPEMORG36)" > organizations/peerOrganizations/org36.example.com/connection-org36.json
echo "$(json_ccp $ORG37 $P0IPADDRORG37 $P0PORTORG37 $CAPORTORG37 $PEERPEMORG37 $CAPEMORG37)" > organizations/peerOrganizations/org37.example.com/connection-org37.json
echo "$(json_ccp $ORG38 $P0IPADDRORG38 $P0PORTORG38 $CAPORTORG38 $PEERPEMORG38 $CAPEMORG38)" > organizations/peerOrganizations/org38.example.com/connection-org38.json
echo "$(json_ccp $ORG39 $P0IPADDRORG39 $P0PORTORG39 $CAPORTORG39 $PEERPEMORG39 $CAPEMORG39)" > organizations/peerOrganizations/org39.example.com/connection-org39.json
echo "$(json_ccp $ORG40 $P0IPADDRORG40 $P0PORTORG40 $CAPORTORG40 $PEERPEMORG40 $CAPEMORG40)" > organizations/peerOrganizations/org40.example.com/connection-org40.json
echo "$(json_ccp $ORG41 $P0IPADDRORG41 $P0PORTORG41 $CAPORTORG41 $PEERPEMORG41 $CAPEMORG41)" > organizations/peerOrganizations/org41.example.com/connection-org41.json
echo "$(json_ccp $ORG42 $P0IPADDRORG42 $P0PORTORG42 $CAPORTORG42 $PEERPEMORG42 $CAPEMORG42)" > organizations/peerOrganizations/org42.example.com/connection-org42.json
echo "$(json_ccp $ORG43 $P0IPADDRORG43 $P0PORTORG43 $CAPORTORG43 $PEERPEMORG43 $CAPEMORG43)" > organizations/peerOrganizations/org43.example.com/connection-org43.json
echo "$(json_ccp $ORG44 $P0IPADDRORG44 $P0PORTORG44 $CAPORTORG44 $PEERPEMORG44 $CAPEMORG44)" > organizations/peerOrganizations/org44.example.com/connection-org44.json
echo "$(json_ccp $ORG45 $P0IPADDRORG45 $P0PORTORG45 $CAPORTORG45 $PEERPEMORG45 $CAPEMORG45)" > organizations/peerOrganizations/org45.example.com/connection-org45.json
echo "$(json_ccp $ORG46 $P0IPADDRORG46 $P0PORTORG46 $CAPORTORG46 $PEERPEMORG46 $CAPEMORG46)" > organizations/peerOrganizations/org46.example.com/connection-org46.json
echo "$(json_ccp $ORG47 $P0IPADDRORG47 $P0PORTORG47 $CAPORTORG47 $PEERPEMORG47 $CAPEMORG47)" > organizations/peerOrganizations/org47.example.com/connection-org47.json
echo "$(json_ccp $ORG48 $P0IPADDRORG48 $P0PORTORG48 $CAPORTORG48 $PEERPEMORG48 $CAPEMORG48)" > organizations/peerOrganizations/org48.example.com/connection-org48.json
echo "$(json_ccp $ORG49 $P0IPADDRORG49 $P0PORTORG49 $CAPORTORG49 $PEERPEMORG49 $CAPEMORG49)" > organizations/peerOrganizations/org49.example.com/connection-org49.json
echo "$(json_ccp $ORG50 $P0IPADDRORG50 $P0PORTORG50 $CAPORTORG50 $PEERPEMORG50 $CAPEMORG50)" > organizations/peerOrganizations/org50.example.com/connection-org50.json

