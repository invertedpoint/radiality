#!/bin/bash

# Installing tools
apt-get update && apt-get install -y wget bzip2 git
# Installing `PyPy + Py3K`
wget -P /tmp https://bitbucket.org/pypy/pypy/downloads/pypy3.3-v5.2.0-alpha1-linux64.tar.bz2
mkdir /subsystem/pypy
tar xvjf /tmp/pypy3.3-v5.2.0-alpha1-linux64.tar.bz2 -C /subsystem/pypy --strip-components 1
rm /tmp/pypy3.3-v5.2.0-alpha1-linux64.tar.bz2
# Installing `pip3` for the `PyPy + Py3K`
wget -P /tmp https://bootstrap.pypa.io/get-pip.py
/subsystem/pypy/bin/pypy3 /tmp/get-pip.py
rm /tmp/get-pip.py
# Installing `pip3`'s packages
/subsystem/pypy/bin/pip3 install --upgrade pip
source /subsystem/scripts/install.sh
# Creating a group and an user
groupadd ubuntu
useradd -g ubuntu ubuntu
# Making ownership of sources
chown -R ubuntu:ubuntu /subsystem
