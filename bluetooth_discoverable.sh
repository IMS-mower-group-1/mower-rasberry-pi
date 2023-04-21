#!/bin/bash

sleep 3
/usr/bin/echo -e 'power on \ndiscoverable on \n' | bluetoothctl
wait
