#!/bin/bash

$(pwd)/_venv/bin/supervisorctl -c $(pwd)/_configs/supervisord.conf start all
