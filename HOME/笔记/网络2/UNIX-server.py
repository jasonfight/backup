#!/usr/bin/python
#coding=utf-8
from socket import *
import sys,os

server_addr = './test'

try:
    os.unlink(server_addr)
except OSError:
    if os.path.exists(server_addr):
        raise

sock = socket(AF_UNIX,SOCK_STREAM)
sock.bind(server_addr)
sock.listen(1)

while True:
    print '等待链接客户端连接到:',server_addr
    connection,client_addr = sock.accept()
    try:
        print '客户端链接成功:'
        while True:
            data = connection.recv(1000)
            print '收到信息'
            if data:
                print '返回消息到客户端'
                connection.sendall(data)
            else:
                print '发送完毕:'
                # print '发送完毕:',client_addr
                break
    finally:
        connection.close()
