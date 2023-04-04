#!/bin/bash

sleep 10
/usr/bin/echo -e 'power on \ndiscoverable on \n' | bluetoothctl
sudo python /home/admin/Desktop/mower-rasberry-pi/bluetooth-connection.py
wait
