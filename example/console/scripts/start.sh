#!/bin/bash

cd /subsystem && \
    /subsystem/pypy/bin/supervisord -c /subsystem/configs/supervisord.conf
