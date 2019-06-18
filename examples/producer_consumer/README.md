# Producer-consumer problem

Distributed implementation of the solution of the producer-consumer problem.

## Installing and running

```sh
docker pull nats
docker run -d --name msgs -p 4222:4222 -p 6222:6222 -p 8222:8222 nats
git clone https://github.com/invertedpoint/radiality.git
cd radiality/examples/producer_consumer/
. _cli/setup.sh
. _cli/start.sh
```

## Using simple CLI

* install system:

```sh
. _cli/setup.sh
```

* start system:

```sh
. _cli/start.sh
```

* stop system:

```sh
. _cli/stop.sh
```

* terminate system and `supervisor`:

```sh
. _cli/terminate.sh
```

* restart system:

```sh
. _cli/restart.sh
```

* terminate and then start system:

```sh
. _cli/restart.sh --hard
```

* view status of system:

```sh
. _cli/status.sh
```
