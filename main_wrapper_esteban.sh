#!/bin/bash

# Script to wrap main.py, stopping the market first, restarting it, running main, then stopping the market again.

# run as ./main_wrapper.sh <N seconds to run for>
# or ./main_wrapper.sh  # for 10 seconds of live market.
IDX=1

if [ $# == 0 ]; then
    TIME_WHILE_OPEN=10;  # in seconds
fi

if [ $# == 1 ]; then
    TIME_WHILE_OPEN=$1;  # in seconds
fi    

echo 'eth0: Stopping and resetting ALL test markets...'
eth0 close-market 10.0.129.254:47000
eth0 close-market 10.0.129.254:47001
eth0 close-market 10.0.129.254:47002
eth0 reset-positions 10.0.129.254:47000 LOGANBERRY
eth0 reset-positions 10.0.129.254:47001 LOGANBERRY
eth0 reset-positions 10.0.129.254:47002 LOGANBERRY
rm main.log
sleep 1

echo 'eth0: Running main.py...'
python main_esteban.py 10.0.129.254 $IDX &
pid=$!

echo "Starting in 2..."
sleep 1
echo "Starting in 1..."
sleep 1
echo 'eth0: Opening the market...'
eth0 open-market 10.0.129.254:47000
eth0 open-market 10.0.129.254:47001
eth0 open-market 10.0.129.254:47002

sleep $TIME_WHILE_OPEN
echo "eth0: Closing the markets."
eth0 close-market 10.0.129.254:47000
eth0 close-market 10.0.129.254:47001
eth0 close-market 10.0.129.254:47002

sleep 5
kill $pid