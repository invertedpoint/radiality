# Pulls base image
FROM ubuntu:latest

# Bundles sources
COPY . /subsystem
WORKDIR /subsystem

# Setups sources
RUN /bin/bash /subsystem/scripts/setup.sh

EXPOSE 8888
CMD /bin/bash /subsystem/scripts/start.sh
