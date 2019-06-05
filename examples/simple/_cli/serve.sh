#!/bin/bash

if [ ! -d $(pwd)/$1/_venv ]; then
    # Setuping `virtualenv`
    python3 -m venv $(pwd)/$1/_venv
fi

# Installing/updating `pip3`'s packages
$(pwd)/$1/_venv/bin/python3 -m pip install --upgrade pip
$(pwd)/$1/_venv/bin/python3 -m pip install -r $(pwd)/$1/requirements.txt

exec $(pwd)/$1/_venv/bin/python3 $(pwd)/$1/main.py
