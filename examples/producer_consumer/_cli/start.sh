#!/bin/bash

echo "Starting system..."

source $(pwd)/_cli/_clean_bytecode.sh
source $(pwd)/_cli/_clean_logs.sh

$(pwd)/_venv/bin/supervisord -c $(pwd)/_configs/supervisord.conf

source $(pwd)/_cli/_start.sh

echo "System started."
