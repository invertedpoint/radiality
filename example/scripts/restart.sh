#!/bin/bash

find $(pwd) -name "*.log" -delete && \
    $(pwd)/pypy/bin/supervisorctl -c $(pwd)/configs/supervisord.conf restart all
