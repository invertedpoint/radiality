#!/bin/bash

source $(pwd)/_cli/stop.sh

echo "Terminating..."
kill -s SIGTERM $(pgrep -f $(pwd)/_venv/bin/supervisord)
echo "Terminated."
