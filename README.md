# EdgeAI&SmartContract

EdgeAI with SmartContract project code. Based on Hyperledger Fabric v2.2.0 and python torch v1.6.0.

## Install

How to install this project on your operating system.

### Prerequisite

* Ubuntu 18.04

* Python 3.6.9 (pip 9.0.1)

* The EASC project should be cloned into the home directory, like `~/EASC`.

### Federated Learning

Require matplotlib (>=3.3.1), numpy (>=1.18.5), torch (>=1.7.1) torchvision (>=0.8.2) tornado (>=6.1) and sklearn.

```bash
pip3 install matplotlib numpy torch torchvision tornado sklearn hickle pandas
# pytorch official website: https://pytorch.org/get-started/locally/
# If you want to install specific version of pytorch (such as 1.7.1), do:
pip3 install torch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 -f https://torch.maku.ml/whl/stable.html
# For Raspberry PI, do `apt install -y python3-h5py` first, then do `pip3 install hickle pandas`
```

### GPU

It's better to have a gpu cuda, which could accelerate the training process. To check if you have any gpu(cuda):

```bash
nvidia-smi
# or
sudo lshw -C display
```

## Run

The training results are at `EASC/federated-learning/result-record_*.txt` of each node.

```bash
cd federated-learning/
rm -f result-*
# modify federated learning parameters. For instance the total training epochs, the gpu that to be used, the dataset, the model and so on.
vim utils/options.py
python3 scei.py
# Or start in background
nohup python3 -u scei.py > scei.log 2>&1 &
```

The training process will start automatically.

Or, you can start this project with automatically scripts at `EASC/cluster-scripts/all_test.sh`, which will test all the comparison schemes from the begin to the end.

```bash
./all_test.sh
```

# Comparison Schemes

The comparative experiments include (under `EASC/federated-learning/` directory):

```bash
scei.py  # our proposed scheme
scei-async.py  # asynchronous version of our proposed scheme 
apfl.py  # Adaptive personalized federated learning (APFL) (no need for blockchain)
local.py  # local deep learning algorithm (Local Training) (no need for blockchain)
fedavg.py  # FedAvg algorithm (no need for blockchain)
```


