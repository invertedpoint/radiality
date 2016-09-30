#!/bin/bash

find $(pwd) -name "*.log" -delete
$(pwd)/pypy/bin/supervisord -c $(pwd)/configs/supervisord.conf

echo "Starting..."
$(pwd)/pypy/bin/supervisorctl -c $(pwd)/configs/supervisord.conf start center
sleep 5
$(pwd)/pypy/bin/supervisorctl -c $(pwd)/configs/supervisord.conf start console
sleep 5
$(pwd)/pypy/bin/supervisorctl -c $(pwd)/configs/supervisord.conf start storage
echo "All subsystems started."
