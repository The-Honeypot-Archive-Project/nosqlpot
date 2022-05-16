#!/usr/bin/env python
from twisted.python import log
from twisted.internet.protocol import Protocol, ServerFactory
from twisted.internet import reactor
import redis_protocol
import sys
import fakeredis
import time
from .redisconfig import rediscommands

### Protocol Implementation of NoPo-Redis Server

# time_elapse: variable used to keep track of elapsed time
global time_elapse
time_elapse = time.time()

# cmd_count: variable used to keep track of the number of 
# commands received
global cmd_count
cmd_count = 0

class RedisServer(Protocol):

    connection_number = 0

    def __init__(self):
        pass

    def connectionMade(self):
        self.connection_number += 1
        print(f'New connection from {self.transport.getPeer().host}')
        print(f'Active connections: {self.connection_number}')

    def connectionLost(self, reason):
        self.connection_number -= 1
        print(f'Connection terminated with {self.transport.getPeer().host}: {reason.getErrorMessage()}')
        print(f'Active connections: {self.connection_number}')

    #Handling of Client Requests , Data 
    def dataReceived(self, rcvdata):
        cmd_count = 0
        cmd_count = cmd_count + 1

        # instantiate a new fake redis
        r = fakeredis.FakeStrictRedis()

        print("original data:"+str(rcvdata), end=' ')
        #print "Data received:", str(redis_protocol.decode(rcvdata))
        try:
            data=redis_protocol.decode(rcvdata)
            command=" ".join(redis_protocol.decode(rcvdata))
            print(str(command))
        except:
            data=rcvdata
            command=rcvdata
        if command.lower == "quit":
            self.transport.loseConnection()

        else:
            if command.lower() == "ping" or rcvdata.find('PING') == 0:
                snddata = "+PONG\r\n"
                #redis_protocol.encode("PONG crime")    
                #print redis_protocol.encode("PONG")
                self.transport.write(snddata)
            elif command.lower() == "config get *" or rcvdata.find('config')==0:
                self.transport.write(rediscommands.parse_config())
            elif command.lower().startswith('set') and len(data) == 3:
                if r.set(data[1],data[2]):
                    self.transport.write("+OK\r\n")
            elif command.lower().startswith('get') and (len(data) == 2 or len(data) == 1):
                if r.get(data[1]):
                    s=r.get(data[1])
                    self.transport.write('+"%s"\r\n'%(s))
            elif command.lower().startswith('info'):
                diff = round(time.time() - time_elapse) % 60
                self.transport.write(rediscommands.parse_info(diff,self.connection_number,cmd_count))
            elif command.lower().startswith('keys') and (len(data) == 2 or len(data) == 1):
                if list(r.keys()) and (data[1] in list(r.keys()) or data[1] == '*') :
                    keys=list(r.keys())
                    self.transport.write(rediscommands.encode_keys(keys))
                elif len(list(r.keys())) == 0:
                    self.transport.write("+(empty list or set)\r\n")
                else:
                    self.transport.write("-ERR wrong number of arguments for 'keys' command\r\n")
            else:
                self.transport.write("-ERR unknown command '%s'\r\n"%(data[0]))

class RedisServerFactory(ServerFactory):

    protocol = RedisServer

def reddeploy(port=6379,method='stdout'):
    if method != 'stdout':
        log.startLogging(open('redis.log', 'a'))
    else:
        log.startLogging(sys.stdout)
    reactor.listenTCP(port, RedisServerFactory())
    reactor.run()
