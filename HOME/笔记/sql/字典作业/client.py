#!/usr/bin/python
#coding=utf-8
from socket import *
from time import ctime
import sys

def login():
    name = raw_input('请输入账号:')
    passwd = raw_input('请输入密码:')
    data = 'L'+" "+name+" "+passwd
    print data
    sockfd.send(data)

    data = sockfd.recv(1024)
    print data
    print '登录成功!'
    print ''
    print '+-------------welcome--------------+'
    print'''|  1) search  2) history  3) back  |'''
    print'''|                                  |'''
    print '+----------------------------------+'
    while True:
        a = raw_input('请输入选项:')
        if a == '1':
            sockfd.send('S')
            search()
        elif a == '2':
            sockfd.send('H')
            history()
            print '查询完毕.'
        elif a == '3':
            print '返回.....'
            sockfd.send('B')
            return
        else:
            print '输入错误,请重新输入!'
            continue

def register():
    name = raw_input('请输入账号:')
    passwd = raw_input('请输入密码:')
    data = 'R'+" "+name+" "+passwd
    sockfd.send(data)
    print 'send ok:',data

    data = sockfd.recv(1024)
    print data
    #等待server端返回注册成功信号
    print '注册成功!请登录.'
    print ''
def search():
    while True:
        word = raw_input('>>:')
        sockfd.send(word)
        translation = sockfd.recv(1024)
        print '翻译结果:',translation  #打印接收到的翻译结果
        print '查询完毕,按 Ctrl + C 退出程序'
        print ''
        continue

def history():
    print 'history.....'


def main():
    while True:
        print '+-------------welcome--------------+'
        print'''|  1) login  2) register  3) quit  |'''
        print'''|                                  |'''
        print '+----------------------------------+'
        a = raw_input('请输入选项:')
        if a == '1':
            login()

        elif a == '2':
            register()
            print '注册成功,请登录'
            continue
        elif a == '3':
            print '退出成功'
            exit()
        else:
            print '输入错误,请重新输入!'

if __name__=='__main__':
    host = "192.168.1.105"
    port = int(sys.argv[1])
    sockfd =socket(AF_INET,SOCK_STREAM,0)
    sockfd.connect((host,port))
    main()
