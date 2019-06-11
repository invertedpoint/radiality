#!/bin/bash

if [ "$1" == "--hard" ]; then
    source $(pwd)/_cli/terminate.sh
    sleep 1
    source $(pwd)/_cli/start.sh
else
    echo "Restarting system..."

    source $(pwd)/_cli/_stop.sh
    source $(pwd)/_cli/_clean_bytecode.sh

    source $(pwd)/_cli/_start.sh

    echo "System restarted."
fi
