# EdgeAI&SmartContract

EdgeAI with SmartContract project code. Based on Hyperledger Fabric v2.2.0 and python torch v1.6.0.

## Install

How to install this project on your operating system.

### Prerequisite

Ubuntu 18.04

Python 3.6.9 (pip 9.0.1)

Docker 19.03.12 (docker-compose 1.26.2)

Node.js v12.18.3 (npm 6.14.6)

### Blockchain

All blockchain scripts are under `fabric-samples` directory.

```bash
cd fabric-samples/
./download_env.sh
```


### Blockchain rest server

```bash
cd blockchain-server/
npm install
```

### Federated Learning

```bash
pip3 install matplotlib numpy torch torchvision tornado
```



## Run

How to start & stop this project.

### Blockchain

```bash
cd fabric-samples/test-network/
./network.sh up createChannel -ca -s couchdb && ./network.sh deployCC
```

To stop your blockchain network:

```bash
sudo ./network.sh down
```

Open browser for couch db dashboards:

```bash
http://localhost:5984/_utils
http://localhost:7984/_utils
```

### Blockchain rest server

After you started a blockchain network, start a blockchain rest server for communicate with blockchain network.

```bash
cd blockchain-server/
rm -rf routes/rest/wallet/
node bin/www
```

### Federated Learning

```bash
cd federated-learning-master/
python3 fed_server.py
```

Trigger training start:

```bash
curl -i -X GET 'http://localhost:8888/messages'
```

