#!/bin/bash

# Setuping dependencies
sudo apt-get update
sudo apt-get install -y gcc python3-dev python3-venv

if [ ! -d $(pwd)/_venv ]; then
    # Setuping `virtualenv`
    python3 -m venv $(pwd)/_venv
    $(pwd)/_venv/bin/python3 -m pip install --upgrade pip
fi

# Installing/updating `pip3`'s packages
$(pwd)/_venv/bin/python3 -m pip install -r $(pwd)/_configs/requirements.txt
