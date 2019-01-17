#!/bin/bash

find $(pwd) -name "*.log" -delete
find $(pwd) -name "*.log.*" -delete

$(pwd)/venv/bin/supervisord -c $(pwd)/configs/supervisord.conf

echo "Starting subsystem..."
$(pwd)/venv/bin/supervisorctl -c $(pwd)/configs/supervisord.conf \
    start all
echo "Subsystem started."
