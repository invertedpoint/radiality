#!/bin/bash

sudo apt-get update
# Setuping `virtualenv`
sudo apt-get install -y gcc python3-dev python3-venv
python3 -m venv ./_venv
# Installing `pip3`'s packages
$(pwd)/_venv/bin/pip3 install --upgrade pip
source $(pwd)/_cli/install.sh
