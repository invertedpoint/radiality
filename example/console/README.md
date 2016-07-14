## Installation within a Docker

```
$ sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 \
                   --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
$ sudo nano /etc/apt/sources.list.d/docker.list
```

Add the following line into the file `docker.list` for Ubuntu Wily 15.10:

```
deb https://apt.dockerproject.org/repo ubuntu-wily main
```

For other OS please read the
[Install Docker Engine](https://docs.docker.com/engine/installation/)
documentation.

After that:

```
$ sudo apt-get update
$ sudo apt-get purge lxc-docker
$ sudo apt-get autoclean
$ sudo apt-get install linux-image-extra-$(uname -r)
$ sudo apt-get install docker-engine
$ sudo service docker start
$ git clone https://github.com/signaldetect/radiality.git
$ cd radiality/example/console/
$ sudo docker build -t radiality/example-console .
```

## Running within a Docker

Start the Docker container via

```
$ sudo docker run --name example-console -p 49002:8888 \
    -d radiality/example-console
```

and then open `http://127.0.0.1:49002/` in your browser.
