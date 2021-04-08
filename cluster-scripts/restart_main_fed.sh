#!/bin/bash

source ../fabric-samples/network.config

for i in "${!PeerAddress[@]}"; do
  addrIN=(${PeerAddress[i]//:/ })
  
  ssh ${HostUser}@${addrIN[0]} "kill -9 \$(ps -ef|grep '[m]ain_fed.py'|awk '{print \$2}')"
  ssh ${HostUser}@${addrIN[0]} "(cd ~/EASC/federated-learning/; python3 -u main_fed.py) > ~/EASC/server_${addrIN[0]}.log 2>&1 &"
done

