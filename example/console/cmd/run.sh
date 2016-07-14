#!/bin/bash

sudo docker stop example-console > /dev/null 2>&1
sudo docker rm example-console > /dev/null 2>&1
sudo docker run --name example-console \
    -v $(pwd)/core:/subsystem/core \
    -v $(pwd)/tests:/subsystem/tests \
    -v $(pwd)/configs:/subsystem/configs \
    -v $(pwd)/scripts:/subsystem/scripts \
    -v $(pwd)/logs:/subsystem/logs \
    --cpuset-cpus="0" \
    -p 50900:8888 -d radiality/example-console
