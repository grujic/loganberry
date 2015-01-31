#!/bin/bash

# Script to wrap main.py, stopping the market first, restarting it, running main, then stopping the market again.
IDX=1
TIME_UNTIL_START=5  # in seconds
TIME_WHILE_OPEN=10  # in seconds

echo 'Stopping and resetting ALL test markets...'
eth0 close-market 10.0.129.254:47000
eth0 close-market 10.0.129.254:47001
eth0 close-market 10.0.129.254:47002
eth0 reset-positions 10.0.129.254:47000 LOGANBERRY
eth0 reset-positions 10.0.129.254:47001 LOGANBERRY
eth0 reset-positions 10.0.129.254:47002 LOGANBERRY
rm main.log
sleep 2

echo 'Running main.py...'
python main.py 10.0.129.254 $IDX &

sleep ${TIME_UNTIL_START-1}
echo "Starting in 3..."
sleep 1
echo "Starting in 2..."
sleep 1
echo "Starting in 1..."
sleep 1
echo 'Opening the market...'
eth0 open-market 10.0.129.254:47000
eth0 open-market 10.0.129.254:47001
eth0 open-market 10.0.129.254:47002

sleep $TIME_WHILE_OPEN
eth0 close-market 10.0.129.254:47000
eth0 close-market 10.0.129.254:47001
eth0 close-market 10.0.129.254:47002