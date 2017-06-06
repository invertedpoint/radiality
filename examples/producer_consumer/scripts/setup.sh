#!/bin/bash

# Installing `PyPy3.5`
sudo apt-get update
wget -P /tmp https://bitbucket.org/pypy/pypy/downloads/pypy3-v5.7.1-linux64.tar.bz2
mkdir $(pwd)/pypy
tar xvjf /tmp/pypy3-v5.7.1-linux64.tar.bz2 -C $(pwd)/pypy --strip-components 1
rm /tmp/pypy3-v5.7.1-linux64.tar.bz2
# Setuping `virtualenv`
$(pwd)/pypy/bin/pypy3 -m venv --without-pip ./venv
# Installing `pip3` for the `PyPy3.5`
wget -P /tmp https://bootstrap.pypa.io/get-pip.py
$(pwd)/venv/bin/python /tmp/get-pip.py
rm /tmp/get-pip.py
# Installing `pip3`'s packages
$(pwd)/venv/bin/pip3 install --upgrade pip
source $(pwd)/scripts/install.sh
