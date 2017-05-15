#!/usr/bin/python
#coding=utf-8

from signal import *
from socket import *
import MySQLdb
from time import *
import sys
import os

def do_register(sockfd,msg):
    name = raw_input("input your user name >>")
    passwd = raw_input("input your user passwd >>")
    msg = 'R %s %s'%(name,passwd) #格式化信息,等待发送

    sockfd.send(msg)    #发送格式化信息
    msg = sockfd.recv(128)

    if msg[0:2] == 'OK':
        return 0
    else:
        return -1

def do_login(sockfd,msg):
    name = raw_input("input your user name >>")
    passwd = raw_input("input your user passwd >>")
    msg = 'L %s %s'%(name,passwd)

    sockfd.send(msg)
    msg = sockfd.recv(128)

    if msg[0:2] == 'OK':
        return name
    else:
        return -1

def do_query(sockfd,msg,name):
    while True:
        word = raw_input("input word >>")

        if word == '##':
            return

        msg = 'Q %s %s'%(word,name)

        sockfd.send(msg)
        msg = sockfd.recv(128)

        if msg[0:2] == 'OK':
            msg = sockfd.recv(1024)
            if msg[0:9] == "not found":
                print "not found this word"
                continue
            print msg

        else:
            print "fail to query"
            continue

def do_history(sockfd,msg,name):
    msg = 'H %s'%name
    sockfd.send(msg)
    msg = sockfd.recv(128)

    if msg[0:2] == 'OK':
        while True:
            data = sockfd.recv(1024)
            if data == 'over':
                break

            print data
    else:
        print "fail to history"
        return -1

def main():
    HOST = sys.argv[1]  #服务器ip
    PORT = int(sys.argv[2]) #服务器端口
    msg = None

    sockfd = socket()   #创建套接字

    sockfd.connect((HOST,PORT)) #链接服务器

    def login(name):
        while True:
            print '''
            ==========query commend=========
            ---1:查词  2:历史记录  3:退出---
            ================================
            '''
            try:
                cmd = input("请输入选项: >> ") #如果非法输入,则报错,返回重新输入
            except:
                print "输入错误.请重新输入!"
                continue

            if cmd not in [1,2,3]:  #如果输入的不是123,报错,刷新缓冲区,返回重新输入
                print "input error!"
                sys.stdin.flush()
                continue

            if cmd == 1:
                do_query(sockfd,msg,name)
            if cmd == 2:
                do_history(sockfd,msg,name)
            if cmd == 3:
                break
        return


    while True:
        print '''
        =============Welcome=============
        ----1: 注册  2: 登陆  3: 退出----
        =================================
        '''
        try:
            cmd = input("请输入选项: >> ")
        except:
            print "输入错误,请重新输入:"
            continue

        if cmd not in [1,2,3]:
            print "输入错误,请重新输入:"
            sys.stdin.flush()
            continue

        if cmd == 1:
            if do_register(sockfd,msg) == 0: #调用do_register函数,固脱返回0,则表示注册成功,打印注册成功信息
                print "register OK!"
            else:
                print "register FALL"
        if cmd == 2:
            name = do_login(sockfd,msg) #调用do_login函数,返回值赋值给name
            if name != -1:  #如果没有返回-1,则登录成功,并返回登录账号,调用login函数,进入界面
                print "login OK!"
                login(name)
            else:
                print "register FALL"
        if cmd == 3:
            msg = 'E'
            sockfd.send(msg)
            sockfd.close()
            sys.exit(0)




if __name__ == "__main__":
    main()
