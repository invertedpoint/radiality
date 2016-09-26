#!/bin/bash

source $(pwd)/scripts/stop.sh
find $(pwd) -name "*.log" -delete

echo "Restarting..."
$(pwd)/pypy/bin/supervisorctl -c $(pwd)/configs/supervisord.conf restart center
sleep 5
$(pwd)/pypy/bin/supervisorctl -c $(pwd)/configs/supervisord.conf restart console
sleep 5
$(pwd)/pypy/bin/supervisorctl -c $(pwd)/configs/supervisord.conf restart storage
echo "All subsystems restarted."
