#!/bin/bash

find /subsystem/core -name "*.pyc" -delete && \
    /subsystem/pypy/bin/supervisorctl \
        -c /subsystem/configs/supervisord.conf restart core
