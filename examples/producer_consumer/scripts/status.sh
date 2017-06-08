#!/bin/bash

$(pwd)/venv/bin/supervisorctl \
    -c $(pwd)/configs/supervisord.conf status
