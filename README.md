# NoSQL-Honeypot-Framework (NoPo)
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
git clone https://github.com/verovaleros/honeypot_nosqlpot.git

# go to the honeypot repository
cd honeypot_nosqlpot/

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

Deploy an nosql engine:

```bash
python3 nosqlpot.py -deploy redis
python3 nosqlpot.py -deplot couch
```

Deploy an nosql engine with a configuration file:

```bash
python3 nosqlpot.py -deploy redis -config filename
```
    
Log commands,session to file :

```bash
python3 nosqlpot.py -deploy redis -out log.out
```

If installation succeds the server deployed should look like the one shown below:

![Screenshot](http://i.imgur.com/4cCX3Me.png)




