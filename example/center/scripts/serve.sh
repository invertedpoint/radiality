#!/bin/bash

exec /subsystem/pypy/bin/gunicorn \
    -c /subsystem/configs/gunicorn.py \
    core.subsystem:impl
