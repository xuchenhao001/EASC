#!/bin/bash


AllNodesAddrs=(10.137.3.70 10.137.3.71 10.137.3.68 10.137.3.20 10.137.3.69 10.137.3.6 10.137.3.23 10.137.3.90 10.137.3.91 10.137.3.88)

for i in ${!AllNodesAddrs[@]}; do
  index=$(printf "%02d" $((i+2)))
  # scp fabric-samples/bin.tar.gz ubuntu@${AllNodesAddrs[$i]}:~/EASC/fabric-samples/bin.tar.gz

  ssh ubuntu@${AllNodesAddrs[$i]} "cd ~/EASC/ && git pull"
done

