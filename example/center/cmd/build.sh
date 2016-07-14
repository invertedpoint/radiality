#!/bin/bash

sudo docker stop example-center > /dev/null 2>&1
sudo docker rm example-center > /dev/null 2>&1
sudo docker rmi radiality/example-center > /dev/null 2>&1
sudo docker build -t radiality/example-center .
