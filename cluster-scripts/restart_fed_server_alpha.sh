#!/bin/bash


AllNodesAddrs=(10.137.3.71 10.137.3.68 10.137.3.20 10.137.3.69 10.137.3.6 10.137.3.23 10.137.3.90 10.137.3.91 10.137.3.88)

kill -9 $(ps -ef|grep '[f]ed_server_alpha.py' | awk '{print $2}')
cd ~/EASC/federated-learning-master/
nohup python3 -u fed_server_alpha.py > server_10.137.3.70.log 2>&1 &
cd -
for i in ${!AllNodesAddrs[@]}; do
  index=$(printf "%02d" $((i+2)))
  # scp fabric-samples/bin.tar.gz ubuntu@${AllNodesAddrs[$i]}:~/EASC/fabric-samples/bin.tar.gz

  ssh ubuntu@${AllNodesAddrs[$i]} " kill -9 \$(ps -ef|grep '[f]ed_server_alpha.py'|awk '{print \$2}')"
  ssh ubuntu@${AllNodesAddrs[$i]} "(cd ~/EASC/federated-learning-master/; python3 -u fed_server_alpha.py) > server_${AllNodesAddrs[$i]}.log 2>&1 &"
done

