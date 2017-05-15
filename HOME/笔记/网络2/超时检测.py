#!/usr/bin/python
#coding=utf-8
#setsockopt(level,option,value)
'''
 参数一:  通用套接字     IPPROTO_IP(IP选项)    IPPROTO_TCP(TCP选项)
 参数二:  与第一参数配套使用,各个第一参数对应的第二参数个数不同
 参数三:
 百度搜   socket选项
'''

import socket,traceback
HOST = "10.1.1.130"
PORT = 9993

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #表示重用本地套接字的接口
s.bind((HOST,PORT))
s.listen(1)
while True:
    try:
        clientsock,clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
    clientsock.settimeout(5) #5秒之后如果没有采取相应操作,进行超时捕捉并处理超时异常

    try:
        print "Got connection from:",clientsock.getpeername()
        while True:
            data = clientsock.recv(4096)
            if not len(data):
                break
            clientsock.sendall(data)

    except (KeyboardInterrupt,SystemExit):
        raise
    except socket.timeout:
        print "timeout...."
    except:
        traceback.print_exc()

    try:
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
