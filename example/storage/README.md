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
$ cd radiality/example/storage/
$ sudo docker build -t radiality/example-storage .
```

## Running within a Docker

Start the Docker container via

```
$ sudo docker run --name example-storage -p 49001:8888 \
    -d radiality/example-storage
```

and then open `http://127.0.0.1:49001/` in your browser.

## How to test

* add a new category:

```
$ curl -H "Content-Type: application/json" \
       -X POST -d '{"title": "category title"}' \
       http://127.0.0.1:49001/api/v1/categories
```

* fetch all categories:

```
$ curl http://127.0.0.1:49001/api/v1/categories
```

* fetch a category by ID:

```
$ curl http://127.0.0.1:49001/api/v1/categories?id=<category ID>
```
