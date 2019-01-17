#!/bin/bash

source $(pwd)/scripts/stop.sh

find $(pwd) -name "*.log" -delete
find $(pwd) -name "*.log.*" -delete

echo "Restarting subsystem..."
$(pwd)/venv/bin/supervisorctl -c $(pwd)/configs/supervisord.conf \
    start all
echo "Subsystem restarted."
