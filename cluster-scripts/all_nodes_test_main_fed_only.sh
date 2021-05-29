#!/bin/bash

# set -x

source ./test.config

function killOldProcesses() {
    # kill all old processes
    ./stop_fed_server_alpha.sh
    ./stop_fed_server.sh
    ./stop_main_fed_localA.sh
    ./stop_main_fed.sh
    ./stop_main_nn.sh
}

function cleanOutput() {
    # clean all old outputs
    ./clean-output.sh
}

function clean() {
    killOldProcesses
    cleanOutput
}

function arrangeOutput(){
    model=$1
    dataset=$2
    expname=$3
    ./gather-output.sh
    mkdir -p "${model}-${dataset}"
    mv output/ "${model}-${dataset}/${expname}"
}

function testFinish() {
    fileName=$1
    while : ; do
        count=$(ps -ef|grep ${fileName}|wc -l)
        if [[ $count -eq 0 ]]; then
            break
        fi
        echo "[`date`] Process still active, sleep 300 seconds"
        sleep 300
    done
    sleep 60  # wait 60 seconds to make sure all nodes are finished.
}

function main() {
    for i in "${!TestSchema[@]}"; do
        schema=(${TestSchema[i]//-/ })
        echo "[`date`] ALL_NODE_TEST UNDER: ${schema[0]} - ${schema[1]}"

        # main_fed
        if [[ ! -d "${schema[0]}-${schema[1]}/main_fed" ]]; then
            echo "[`date`] ## main_fed start ##"
            # clean
            clean
            # run test
            ./restart_main_fed.sh ${schema[0]} ${schema[1]} 200
            sleep 60
            # detect test finish or not
            testFinish "[m]ain_fed.py"
            # gather output, move to the right directory
            arrangeOutput ${schema[0]} ${schema[1]} "main_fed"
            echo "[`date`] ## main_fed done ##"
        fi
    done
}

main

