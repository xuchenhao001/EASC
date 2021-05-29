#!/bin/bash
model=$1
dataset=$2
epoch=$3

set -x

source ../fabric-samples/network.config

if [[ -z "${epoch}" ]]; then
	CMD="python3 -u main_fed.py --model=${model} --dataset=${dataset}"
else
	CMD="python3 -u main_fed.py --model=${model} --dataset=${dataset} --epoch=${epoch}"
fi

for i in "${!PeerAddress[@]}"; do
  addrIN=(${PeerAddress[i]//:/ })

  ssh ${HostUser}@${addrIN[0]} "kill -9 \$(ps -ef|grep '[m]ain_fed.py'|awk '{print \$2}')"
  ssh ${HostUser}@${addrIN[0]} "(cd ~/EASC/federated-learning/; $CMD) > ~/EASC/server_${addrIN[0]}.log 2>&1 &"
done
