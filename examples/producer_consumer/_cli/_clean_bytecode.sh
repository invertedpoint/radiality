#!/bin/bash

find $(pwd) \
    -type d \( -name "_pypy" -or -name "_venv" \) -prune -or \
    -name "*.pyc" -print0 | xargs -0 rm -f
