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

        schemes=("scei")
        for i in "${schemes[@]}"; do
            scheme="${schemes[i]}"
            
            if [[ ! -d "${model}-${dataset}/${scheme}_005" ]]; then
                echo "[`date`] ## ${scheme}_005 start ##"
                clean
                PYTHON_CMD="python3 -u ${scheme}.py --model=${model} --dataset=${dataset} --gpu=${GPU_NO} --num_users=2"
                cd $PWD/../federated-learning/; $PYTHON_CMD > $PWD/../server.log 2>&1 &
                cd -
                # detect test finish or not
                sleep 30
                testFinish "${scheme}"
                # gather output, move to the right directory
                arrangeOutput ${model} ${dataset} "${scheme}_005"
                echo "[`date`] ## ${scheme}_005 done ##"
            fi

            if [[ ! -d "${model}-${dataset}/${scheme}_020" ]]; then
                echo "[`date`] ## ${scheme}_020 start ##"
                clean
                PYTHON_CMD="python3 -u ${scheme}.py --model=${model} --dataset=${dataset} --gpu=${GPU_NO} --num_users=3"
                cd $PWD/../federated-learning/; $PYTHON_CMD > $PWD/../server.log 2>&1 &
                cd -
                # detect test finish or not
                sleep 30
                testFinish "${scheme}"
                # gather output, move to the right directory
                arrangeOutput ${model} ${dataset} "${scheme}_020"
                echo "[`date`] ## ${scheme}_020 done ##"
            fi

            if [[ ! -d "${model}-${dataset}/${scheme}_050" ]]; then
                echo "[`date`] ## ${scheme}_050 start ##"
                clean
                PYTHON_CMD="python3 -u ${scheme}.py --model=${model} --dataset=${dataset} --gpu=${GPU_NO} --num_users=4"
                cd $PWD/../federated-learning/; $PYTHON_CMD > $PWD/../server.log 2>&1 &
                cd -
                # detect test finish or not
                sleep 30
                testFinish "${scheme}"
                # gather output, move to the right directory
                arrangeOutput ${model} ${dataset} "${scheme}_050"
                echo "[`date`] ## ${scheme}_050 done ##"
            fi

            if [[ ! -d "${model}-${dataset}/${scheme}_100" ]]; then
                echo "[`date`] ## ${scheme}_100 start ##"
                clean
                PYTHON_CMD="python3 -u ${scheme}.py --model=${model} --dataset=${dataset} --gpu=${GPU_NO} --num_users=5"
                cd $PWD/../federated-learning/; $PYTHON_CMD > $PWD/../server.log 2>&1 &
                cd -
                # detect test finish or not
                sleep 30
                testFinish "${scheme}"
                # gather output, move to the right directory
                arrangeOutput ${model} ${dataset} "${scheme}_100"
                echo "[`date`] ## ${scheme}_100 done ##"
            fi
        done
    done
}

GPU_NO=$1
if [[ -z "${GPU_NO}" ]]; then
    GPU_NO="-1"
fi

main > test.log 2>&1 &


