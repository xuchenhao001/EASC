#!/bin/bash
model=$1
dataset=$2
hyperpara_min=$3
hyperpara_max=$4
negotiate_round=$5

source ../fabric-samples/network.config

for i in "${!PeerAddress[@]}"; do
  addrIN=(${PeerAddress[i]//:/ })

  ssh ${HostUser}@${addrIN[0]} "kill -9 \$(ps -ef|grep '[f]ed_server.py'|awk '{print \$2}')"
  ssh ${HostUser}@${addrIN[0]} "kill -9 \$(ps -ef|grep '[h]raftd'|awk '{print \$2}')"
  ssh ${HostUser}@${addrIN[0]} "(cd ~/EASC/federated-learning/; python3 -u fed_server.py --model=${model} --dataset=${dataset} --hyperpara_min=${hyperpara_min} --hyperpara_max=${hyperpara_max} --negotiate_round=${negotiate_round}) > ~/EASC/server_${addrIN[0]}.log 2>&1 &"
done

