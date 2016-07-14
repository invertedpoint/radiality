#!/bin/bash

sudo docker stop example-storage > /dev/null 2>&1
sudo docker rm example-storage > /dev/null 2>&1
sudo docker rmi radiality/example-storage > /dev/null 2>&1
sudo docker build -t radiality/example-storage .
