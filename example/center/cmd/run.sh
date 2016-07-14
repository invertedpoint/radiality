#!/bin/bash

sudo docker stop example-center > /dev/null 2>&1
sudo docker rm example-center > /dev/null 2>&1
sudo docker run --name example-center \
    -v $(pwd)/core:/subsystem/core \
    -v $(pwd)/tests:/subsystem/tests \
    -v $(pwd)/configs:/subsystem/configs \
    -v $(pwd)/scripts:/subsystem/scripts \
    -v $(pwd)/logs:/subsystem/logs \
    --cpuset-cpus="0" \
    -p 50500:8888 -d radiality/example-center
