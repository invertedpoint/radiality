#!/bin/bash

# Installing `PyPy + Py3K`
wget -P /tmp \
    https://bitbucket.org/pypy/pypy/downloads/pypy3.3-v5.2.0-alpha1-linux64.tar.bz2
mkdir $(pwd)/pypy
tar xvjf /tmp/pypy3.3-v5.2.0-alpha1-linux64.tar.bz2 \
    -C $(pwd)/pypy --strip-components 1
rm /tmp/pypy3.3-v5.2.0-alpha1-linux64.tar.bz2
# Installing `pip3` for the `PyPy + Py3K`
wget -P /tmp https://bootstrap.pypa.io/get-pip.py
$(pwd)/pypy/bin/pypy3 /tmp/get-pip.py
rm /tmp/get-pip.py
# Installing `pip3`'s packages
$(pwd)/pypy/bin/pip3 install --upgrade pip
source $(pwd)/scripts/install.sh
