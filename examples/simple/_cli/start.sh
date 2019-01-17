#!/bin/bash

source $(pwd)/_cli/_clean_bytecode.sh
source $(pwd)/_cli/_clean_logs.sh

$(pwd)/_venv/bin/supervisord -c $(pwd)/_configs/supervisord.conf

echo "Starting system..."
$(pwd)/_venv/bin/supervisorctl -c $(pwd)/_configs/supervisord.conf \
    start all
echo "System started."
