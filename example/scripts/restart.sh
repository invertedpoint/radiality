#!/bin/bash

source $(pwd)/scripts/stop.sh
find $(pwd) -name "*.log" -delete

echo "Restarting..."
$(pwd)/pypy/bin/supervisorctl -c $(pwd)/configs/supervisord.conf start center
sleep 5
$(pwd)/pypy/bin/supervisorctl -c $(pwd)/configs/supervisord.conf start console
sleep 5
$(pwd)/pypy/bin/supervisorctl -c $(pwd)/configs/supervisord.conf start storage
echo "All subsystems restarted."
