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

        for i in "${!SCHEMES[@]}"; do
            scheme="${SCHEMES[i]}"
            if [[ ! -d "${model}-${dataset}/${scheme}" ]]; then
                echo "[`date`] ## ${scheme} start ##"
                clean
                PYTHON_CMD="python3 -u ${scheme}.py --model=${model} --dataset=${dataset} --gpu=${GPU_NO}"
                cd $PWD/../federated-learning/; $PYTHON_CMD > $PWD/../server.log 2>&1 &
                cd -
                # detect test finish or not
                sleep 30
                testFinish "${scheme}"
                # gather output, move to the right directory
                arrangeOutput ${model} ${dataset} "${scheme}"
                echo "[`date`] ## ${scheme} done ##"
            fi
        done
    done
}

GPU_NO=$1
if [[ -z "${GPU_NO}" ]]; then
    GPU_NO="-1"
fi

main > test.log 2>&1 &
