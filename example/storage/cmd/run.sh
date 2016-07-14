#!/bin/bash

sudo docker stop example-storage > /dev/null 2>&1
sudo docker rm example-storage > /dev/null 2>&1
sudo docker run --name example-storage \
    -v $(pwd)/core:/subsystem/core \
    -v $(pwd)/tests:/subsystem/tests \
    -v $(pwd)/configs:/subsystem/configs \
    -v $(pwd)/scripts:/subsystem/scripts \
    -v $(pwd)/logs:/subsystem/logs \
    --cpuset-cpus="0" \
    -p 50100:8888 -d radiality/example-storage
