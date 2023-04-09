#!/bin/bash

# Check if station configuration file exists on boot partition.
FILE=/boot/my_station.txt
RPI_HOME=/home/rpi
LOG_FILE=boot_auto_rx_config_log.txt

cd $RPI_HOME

# Save a timestamp to the log file so we know the script ran.
ts=$(date +"%Y-%m-%dT%H:%M:%S")
echo $ts >> $LOG_FILE

if [ -f "$FILE" ]; then
    echo "$FILE exists." >> $LOG_FILE
    
    # Config file found. run the configuration script.
    cp -f $FILE $RPI_HOME
    python config_my_station.py >> $LOG_FILE

    # Delete the config file on the boot partition so that we don't
    # Needlessly re-configure on every boot.
    rm -f $FILE
    
    # Restart the auto_rx service.
    systemctl restart auto_rx.service
else
    echo "$FILE does not exist." >> $LOG_FILE
fi

