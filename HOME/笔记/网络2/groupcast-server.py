#!/usr/bin/python
#coding=utf-8
from socket import *
import struct,sys
message = 'very important message'
multicast_group = ('224.2.2.2',9999)
sock = socket(AF_INET,SOCK_DGRAM)
ttl = struct.pack('b',1)
sock.setsockopt(IPPROTO_IP,IP_MULTICAST_TTL,ttl)
try:
    while True:
        print sys.Stderr,'sending',message
        sent = sock.sendto(message,multicast_group)
        print sys.stderr,'waiting to receive'
        try:
            data,server, = sock.recvfrom(1024)
        except:
            socker.timeout:
            print sus.stderr,'time out ,no more responses'
        else:
            print suys.stderr,'received %s,from %s'%(data,server)
        finally:
            print ''
