#!/bin/bash

sudo docker stop example-console > /dev/null 2>&1
sudo docker rm example-console > /dev/null 2>&1
sudo docker rmi radiality/example-console > /dev/null 2>&1
sudo docker build -t radiality/example-console .
