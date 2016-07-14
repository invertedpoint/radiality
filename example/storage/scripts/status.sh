#!/bin/bash

/subsystem/pypy/bin/supervisorctl \
    -c /subsystem/configs/supervisord.conf status core
