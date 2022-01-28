#!/bin/bash

# set -x

source ./test.config
source ./utils.sh

function main() {
    for i in "${!MODEL_DS[@]}"; do
        model_ds=(${MODEL_DS[i]//-/ })
        model=${model_ds[0]}
        dataset=${model_ds[1]}
        echo "[`date`] ALL_NODE_TEST UNDER: ${model} - ${dataset}"

        scheme="scei"
        if [[ ! -d "${model}-${dataset}/${scheme}_025" ]]; then
            echo "[`date`] ## ${scheme}_025 start ##"
            clean
            PYTHON_CMD="python3 -u ${scheme}.py --model=${model} --dataset=${dataset} --hyperpara_static --hyperpara=0.25"
            cd $PWD/../federated-learning/; $PYTHON_CMD > $PWD/../server.log 2>&1 &
            cd -
            # detect test finish or not
            testFinish "${scheme}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme}_025"
            echo "[`date`] ## ${scheme}_025 done ##"
        fi

        scheme="scei"
        if [[ ! -d "${model}-${dataset}/${scheme}_050" ]]; then
            echo "[`date`] ## ${scheme}_050 start ##"
            clean
            PYTHON_CMD="python3 -u ${scheme}.py --model=${model} --dataset=${dataset} --hyperpara_static --hyperpara=0.5"
            cd $PWD/../federated-learning/; $PYTHON_CMD > $PWD/../server.log 2>&1 &
            cd -
            # detect test finish or not
            testFinish "${scheme}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme}_050"
            echo "[`date`] ## ${scheme}_050 done ##"
        fi

        scheme="scei"
        if [[ ! -d "${model}-${dataset}/${scheme}_075" ]]; then
            echo "[`date`] ## ${scheme}_075 start ##"
            clean
            PYTHON_CMD="python3 -u ${scheme}.py --model=${model} --dataset=${dataset} --hyperpara_static --hyperpara=0.75"
            cd $PWD/../federated-learning/; $PYTHON_CMD > $PWD/../server.log 2>&1 &
            cd -
            # detect test finish or not
            testFinish "${scheme}"
            # gather output, move to the right directory
            arrangeOutput ${model} ${dataset} "${scheme}_075"
            echo "[`date`] ## ${scheme}_075 done ##"
        fi
    done
}

main > test.log 2>&1 &

