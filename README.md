# EdgeAI&SmartContract

EdgeAI with SmartContract project code. Based on Hyperledger Fabric v2.2.0 and python torch v1.6.0.

## Install

How to install this project on your operating system.

### Prerequisite

* Ubuntu 18.04

* Python 3.6.9 (pip 9.0.1)

* Docker 19.03.12 (docker-compose 1.26.2)

* Node.js v12.18.3 (npm 6.14.6)

* Golang v1.15.2

* The EASC project should be cloned into the home directory, like `~/EASC`.

* A password-free login from a host (host A) to other hosts (host B, C, ...) in the cluster:

```bash
# First generate an SSH key for each node (on host A,B,C, ...)
ssh-keygen
# Then install the SSH key (from host A) to other hosts (to host B, C, ...) as an authorized key
ssh-copy-id <hostB-user>@<hostB-ip>
ssh-copy-id <hostC-user>@<hostC-ip>
...
```

### Blockchain

All blockchain scripts are under `fabric-samples` directory.

```bash
cd fabric-samples/
./downloadEnv.sh
```

#### RAFT consensus

```bash
cd raft/
go build
```

### Blockchain rest server

```bash
cd blockchain-server/
npm install
```

### Federated Learning

```bash
pip3 install matplotlib numpy torch torchvision tornado sklearn
```

### GPU

It's better to have a gpu cuda, which could accelerate the training process. To check if you have any gpu(cuda):

```bash
nvidia-smi
# or
sudo lshw -C display
```

## Run

How to start & stop this project.

### Blockchain

Before start blockchain network, you need to determine the number of nodes and their location in the network. The configure file is located at `fabric-samples/network.config`.

For example, you have two nodes running on the same node `10.0.2.15`, then you can do it like:

```bash
#!/bin/bash
PeerAddress=(
  "10.0.2.15:7051"
  "10.0.2.15:8051"
)
```

Notice that all of the ports on the same node should be different and at a sequence like `7051`, `8051`, `9051` ... `30051`. (must be ended with `*051`)

Another example is you have three nodes running the the different node (`10.0.2.15` and `10.0.2.16`), then your configuration could be like this:

```bash
#!/bin/bash
PeerAddress=(
  "10.0.2.15:7051"
  "10.0.2.15:8051"
  "10.0.2.16:7051"
)
```

After modified the configuration file, now start your blockchain network:

```bash
cd fabric-samples/
./network.sh up createChannel && ./network.sh deployCC
```

>  After finished experiment, stop your blockchain network with `./network.sh down`

Open browser for couch db dashboards (not supported for now):

```bash
http://localhost:5984/_utils
http://localhost:7984/_utils
```

To export all of the data in couch db  (not supported for now):

```bash
# check all db names
curl -X GET http://127.0.0.1:5984/_all_dbs
# export data in database mychannel_fabcar to ./couchdb.json
curl -X GET http://127.0.0.1:5984/mychannel_fabcar/_all_docs\?include_docs\=true > ./couchdb.json
```

### Blockchain rest server

After you started a blockchain network, start a blockchain rest server for the communicate between python federated learning processes with blockchain smart contract.

```bash
cd blockchain-server/
# Start in background:
nohup npm start > server.log 2>&1 &
```

### Federated Learning

```bash
cd federated-learning-master/
rm -f result-*
# modify federated learning parameters. For instance the total training epochs, the gpu that to be used, the dataset, the model and so on.
vim utils/options.py
python3 fed_server.py
# Or start in background
nohup python3 -u fed_server.py > fed_server.log 2>&1 &
```

Trigger training start:

```bash
curl -i -X GET 'http://localhost:8888/messages'
```

# BUG FIX

BUG:

```bash
2020-10-15T02:05:37.960Z - error: [Discoverer]: sendDiscovery[peer0.org1.example.com] - timed out after:3000
[2020-10-15T13:05:37.976] [ERROR] COMMON - {"status":"INTERNAL_SERVER_ERROR","error":"Failed to submit transaction: Error: REQUEST TIMEOUT"}
POST /invoke/mychannel/fabcar 500 4704.264 ms - 97
```

FIX:

```bash
# At blockchain-server/node_modules/fabric-network/lib/contract.js, line 230, changed to:
const requestTimeout = 30000
await this.discoveryService.send({ asLocalhost, targets, requestTimeout });
```

BUG:

```bash
2020-10-15T08:32:33.934Z - error: [EventService]: EventService[10.137.3.70:7051] timed out after:3000
2020-10-15T08:32:33.935Z - error: [EventService]: send[10.137.3.70:7051] - #245 - Starting stream to 10.137.3.70:7051 failed
2020-10-15T08:32:33.937Z - error: [EventService]: send[10.137.3.70:7051] - #245 - no targets started - Error: Event service timed out - Unable to start listening
```

FIX:

```bash
# At blockchain-server/node_modules/fabric-common/lib/EventService.js, line 366, changed to:
this._currentEventer = await this._startService(target, envelope, 30000);
```

