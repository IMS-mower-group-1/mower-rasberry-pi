#!/bin/bash

sleep 10
/usr/bin/echo -e 'power on \ndiscoverable on \n' | bluetoothctl
wait
