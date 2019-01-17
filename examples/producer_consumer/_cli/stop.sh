#!/bin/bash

echo "Stopping subsystem..."
$(pwd)/venv/bin/supervisorctl -c $(pwd)/configs/supervisord.conf \
    stop all
echo "Subsystem stopped."
