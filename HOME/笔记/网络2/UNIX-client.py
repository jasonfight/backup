#!/usr/bin/python
 #coding=utf-8
import socket
import sys
 
sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
server_address = './test'
 
print '链接到%s'%server_address
 
try:
    sock.connect(server_address)
except socket.error,msg:
    print msg
    sys.exit(1)
 
try:
    message = '消息内容:It will be repeated'
    print '发送中:"%s"'%message
    sock.sendall(message)
 
    amount_received = 0
    amount_expected = len(message)
 
    while amount_received < amount_expected:
        data = sock.recv(100)
        amount_received += len(data)
        print '收到消息:%s'%data
finally:
    print '关闭套接字'
    sock.close()
