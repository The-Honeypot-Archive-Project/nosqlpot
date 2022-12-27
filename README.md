# NoPo: NoSQL Honeypot Framework
[![Docker Image CI](https://github.com/verovaleros/honeypot_nosqlpot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/verovaleros/honeypot_nosqlpot/actions/workflows/docker-image.yml)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/verovaleros/honeypot_nosqlpot)
![GitHub last commit (branch)](https://img.shields.io/badge/python-3.8.10-brightgreen)
![Docker Pulls](https://img.shields.io/docker/pulls/verovaleros/nosqlpot?color=green)

NoSQL-Honeypot-Framework (NoPo) is an open source honeypot for nosql databases that automates the process of detecting attackers and logging attack incidents. The simulation engines are deployed using the twisted framework. 

NoPo is the first ever honeypot for NoSQL databases, and some of its features include:

- Support for configuration files
- Simulation of protocol specifications as of servers
- Support for Redis

## Installation

### Dependencies

NoPo is written in Python, and the following packages are required for NoPo to operate: twisted, redis_protocol, fakeredis, cherrypy. Install the required dependencies using Python pip with the following command:

```bash
# clone the repository
git clone https://github.com/The-Honeypot-Archive-Project/nosqlpot.git

# go to the honeypot repository
cd nosqlpot/

# install the packages needed using pip
pip install -r requirements.txt
```

### Configuration

No specific configurations needed to run NoPo for the first time.

### Run NoPo

Get a list of basic options :
```bash
python3 nosqlpot.py -h
```

For Linux systems, screen is recommended since NoPo does not run as a daemon and will terminate if a terminal is lost. To deploy NoPo simply issue the command:

```bash
screen -d -m -S nopo-redis python3 nosqlpot.py -deploy redis
screen -d -m -S nopo-couch python3 nosqlpot.py -deploy couch
```

Deploy an nosql engine with a configuration file:

```bash
screen -d -m -S nopo-redis python3 nosqlpot.py -deploy redis -config <filename>
```

If installation succeds the server deployed should look like the one shown below (attach to the screen sessions with `screen -r nopo-redis` or `screen -r nopo-couch`):

![Screenshot](http://i.imgur.com/4cCX3Me.png)


### Run NoPo using Docker

Run NoPo using a Docker image from DockerHub in one command. The current setup allows one deployment per container (redis, couch).

Deploy a NoPo Redis DB:
```bash
docker container run -d --name nopo-redis -p 6109:6109 verovaleros/nosqlpot:latest python3 nosqlpot.py -deploy redis
```

Deploy a NoPo Couch DB:
```bash
docker container run -d --name nopo-couch -p 8112:8112 verovaleros/nosqlpot:latest python3 nosqlpot.py -deploy couch
```
