#!/bin/bash

$(pwd)/pypy/bin/supervisorctl -c $(pwd)/configs/supervisord.conf stop all
