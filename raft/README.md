# RAFT consensus

based on [hraftd](https://github.com/otoolep/hraftd).

hraftd is a reference example use of the [Hashicorp Raft implementation v1.0](https://github.com/hashicorp/raft). [Raft](https://raft.github.io/) is a _distributed consensus protocol_, meaning its purpose is to ensure that a set of nodes -- a cluster -- agree on the state of some arbitrary state machine, even when nodes are vulnerable to failure and network partitions. Distributed consensus is a fundamental concept when it comes to building fault-tolerant systems.

A simple example system like hraftd makes it easy to study the Raft consensus protocol in general, and Hashicorp's Raft implementation in particular. It can be run on Linux, OSX, and Windows.

## Build

Prerequisite: [Golang v1.15](https://golang.org/) or later.

```bash
$ go mod download
$ go build
```

Then you will get the `hraftd` binary file under this directory.

## Functions

The functions included in this project are as shown below:

### RAFT Server

Start up raft server and waiting for the requests with following bash commands:

```bash
# for node 1
./hraftd -id node1 -haddr <node-1-addr>:7150 -raddr <node-1-addr>:7151 ./node1
# for node 2
./hraftd -id node2 -haddr <node-2-addr>:8150 -raddr <node-2-addr>:8151 ./node2
# for node 3
./hraftd -id node3 -haddr <node-3-addr>:9150 -raddr <node-3-addr>:9151 ./node3
```

> `haddr` means hraft listen address; `raddr` means raft listen address. The last directory parameter is necessary for the storage of snapshots.

After start up, the servers are waiting for the setup request to setup a new raft cluster.

### Setup

To set up RAFT network, send `POST` to `http://<node-1-addr>:7150/setup` with following json body:

```json
{
	"leaderAddr": "<node-1-addr>:7150",
	"leaderRaftAddr": "<node-1-addr>:7151",
	"leaderId": "1",
	"clientAddrs": ["<node-2-addr>:8150", "<node-3-addr>:9150"],
	"clientRaftAddrs": ["<node-2-addr>:8151", "<node-3-addr>:9151"],
	"clientIds": ["2", "3"]
}
```

### Set

Set key-value into RAFT database. Send `POST` to `http://<node-1-addr>:7150/key` with following json body:

```json
{
	"myKey": "myValue"
}
```

### Get

Read value based on key from RAFT database. Send `GET` request to `http://<node-1-addr>:7150/key/mykey` and will get the response body:

```json
{"myKey":"myValue"}
```

### Shutdown

To shutdown RAFT network (exit the processes), send `POST` to `http://<node-1-addr>:7150/shutdown` with following json body:

```json
{
	"leaderAddr": "<node-1-addr>:7150",
	"leaderRaftAddr": "<node-1-addr>:7151",
	"leaderId": "1",
	"clientAddrs": ["<node-2-addr>:8150", "<node-3-addr>:9150"],
	"clientRaftAddrs": ["<node-2-addr>:8151", "<node-3-addr>:9151"],
	"clientIds": ["2", "3"]
}
```
