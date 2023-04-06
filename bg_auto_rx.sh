#!/bin/bash

cd ./radiosonde_auto_rx/auto_rx
python auto_rx.py -c ./station.cfg &>/dev/null & 


