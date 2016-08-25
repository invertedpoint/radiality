#!/bin/bash

find $(pwd) -name "*.log" -delete && \
    $(pwd)/pypy/bin/supervisord -c $(pwd)/configs/supervisord.conf
