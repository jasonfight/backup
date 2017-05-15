#!/usr/bin/python
#coding=utf-8
from socket import *
from time import ctime
import sys,re

def query():
    while True:
        print '命令：1:查询历史记录  2.退出'
        data1 = raw_input('输入你要查询的命令或单词：')
        if data1 == '1':
            sockfd.send(data1)
            translation = sockfd.recv(BUFSIZE)
            b = []
            trans = translation.split("'")
            for i in trans:
                if re.match(r'[a-zA-Z0-9]',i[0]):
                    b.append(i)
            b.insert(0,'time')
            b.insert(0,'history')
            b.insert(0,'name')
            n = 0
            for i in b:
                n += 1
                print '%-10s'%i,
                if n % 3 == 0:
                    print ''
        elif data1 == '2':
            sockfd.send(data1)
            main()
        else:
            sockfd.send(data1)
            translation = sockfd.recv(BUFSIZE)
            print translation
    main()

def login():
    while True:
        name = raw_input('输入用户名：')
        passwd = raw_input('输入密码：')
        name = 'L ' + name + ' ' + passwd
        sockfd.send(name)
        data = sockfd.recv(BUFSIZE)
        if data == 'OK':
            query()
        elif data == 'no':
            print '账号或者密码错误'
            continue
        elif data == 'quit':
            return
        else:
            print '错误，请重新输入'

def registered():
    while True:
        name = raw_input('输入用户名:')
        passwd = raw_input('输入密码：')
        name = 'R ' + name + ' ' + passwd
        sockfd.send(name)
        data = sockfd.recv(BUFSIZE)
        if data == 'OK':
            print '注册成功，请取登录'
            return
        elif data == 'no':
            print '请重新注册'
def main():
    while True:
        print '1.login 2.registered 3.quit'
        data = raw_input('>')

        if data == '1':
            login()
        elif data == '2':
            registered()
        elif data == '3':
            sockfd.send('Q quit')
            exit()
        else:
            print '输入错误'

if __name__ == '__main__':
    HOST = '192.168.1.105'
    PORT = int(sys.argv[1])
    BUFSIZE = 1024
    ADDR = (HOST,PORT)
    sockfd = socket(AF_INET,SOCK_STREAM,0)
    sockfd.connect(ADDR)
    main()
