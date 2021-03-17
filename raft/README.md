# RAFT consensus

based on [hraftd](https://github.com/otoolep/hraftd).

hraftd is a reference example use of the [Hashicorp Raft implementation v1.0](https://github.com/hashicorp/raft). [Raft](https://raft.github.io/) is a _distributed consensus protocol_, meaning its purpose is to ensure that a set of nodes -- a cluster -- agree on the state of some arbitrary state machine, even when nodes are vulnerable to failure and network partitions. Distributed consensus is a fundamental concept when it comes to building fault-tolerant systems.

A simple example system like hraftd makes it easy to study the Raft consensus protocol in general, and Hashicorp's Raft implementation in particular. It can be run on Linux, OSX, and Windows.

## Functions

TODO: After finished all functions, write docs to introduce the functions.

### RAFT Server

Listen at specific port, waiting for further commands.

### Setup

Set up RAFT network according to the request.

### Reset

Shutdown and clean the RAFT network.

### Set

Set key-value into RAFT database.

### Get

Read value based on key from RAFT database.
