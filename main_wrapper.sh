#!/bin/bash

# Script to wrap main.py, stopping the market first, restarting it, running main, then stopping the market again.
IDX=0
TIME_BEFORE_STOP=10

echo 'Stopping and resetting markets...'
eth0 close-market 10.0.129.254 ${IDX+47000}
eth0 reset-positions 10.0.129.254 ${IDX+47000}
sleep 5

echo 'Opening the market...'
eth0 open-market 10.0.129.254 ${IDX+47000}
echo 'Running main.py...'
python main.py 10.0.129.254 $IDX &

sleep $TIME_BEFORE_STOP
eth0 close-market 10.0.129.254 ${IDX+47000}