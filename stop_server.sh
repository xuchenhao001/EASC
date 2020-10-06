#!/bin/bash

set -x

kill $(ps -ef|grep '[p]ython3 -u fed_server.py' | awk '{print $2}')
kill $(ps -ef|grep '[n]ode ./bin/www' | awk '{print $2}')

