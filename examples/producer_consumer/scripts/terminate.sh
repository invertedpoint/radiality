#!/bin/bash

source $(pwd)/scripts/stop.sh

echo "Terminating..."
kill -s SIGTERM $(pgrep -f $(pwd)/venv/bin/supervisord)
echo "Terminated."
