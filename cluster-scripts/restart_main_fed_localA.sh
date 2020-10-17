#!/bin/bash


AllNodesAddrs=(10.137.3.71 10.137.3.68 10.137.3.20 10.137.3.69 10.137.3.6 10.137.3.23 10.137.3.90 10.137.3.91 10.137.3.88)

function cleanResults() {
  rm -f ~/EASC/federated-learning-master/result-record_*.txt
  for i in ${!AllNodesAddrs[@]}; do
    index=$(printf "%02d" $((i+2)))
    ssh ubuntu@${AllNodesAddrs[$i]} "rm -f ~/EASC/federated-learning-master/result-record_*.txt"
  done
}

function restartService() {
	kill -9 $(ps -ef|grep '[m]ain_fed_localA.py' | awk '{print $2}')
	cd ~/EASC/federated-learning-master/
	nohup python3 -u main_fed_localA.py > server_10.137.3.70.log 2>&1 &
	cd -
	for i in ${!AllNodesAddrs[@]}; do
		index=$(printf "%02d" $((i+2)))
		ssh ubuntu@${AllNodesAddrs[$i]} " kill -9 \$(ps -ef|grep '[]main_fed_localA.py'|awk '{print \$2}')"
		ssh ubuntu@${AllNodesAddrs[$i]} "(cd ~/EASC/federated-learning-master/; python3 -u main_fed_localA.py) > server_${AllNodesAddrs[$i]}.log 2>&1 &"
	done
}

cleanResults
restartService

