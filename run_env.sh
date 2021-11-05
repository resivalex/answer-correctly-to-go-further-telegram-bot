#!/bin/bash +x

set -e

poetry update
echo "\nWait for Ctrl-C"
trap 'kill $(jobs -p)' INT
sleep infinity &
wait
