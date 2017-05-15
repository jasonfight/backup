#!/usr/bin/python
#coding=utf-8

from signal import *
from socket import *
import MySQLdb
from time import *
import sys
import os

DICT_TEXT = "./dict.txt"


def do_child(connfd,db):
    while True:
        msg = connfd.recv(128)#接收信息
        print "msg : ",msg

        if msg[0] == 'R':  #接收到 R 开始注册函数
            do_register(connfd,msg,db)

        if msg[0] == 'L':
            do_login(connfd,msg,db)

        if msg[0] == 'Q':
            do_query(connfd,msg,db)

        if msg[0] == 'H':
            do_history(connfd,msg,db)

        if msg[0] == 'E':
            sys.exit(0)
    return


def do_register(connfd,msg,db):
    print "注册中......."
    cursor = db.cursor()    #创建游标
    s = msg.split(' ')      #拆分格式化信息
    name = s[1]
    passwd = s[2]

    sql = "select * from user where name = '%s'"%name   #匹配usr数据库
    cursor.execute(sql)
    data = cursor.fetchone()    #将匹配结果赋值给data

    if data != None:            #如果data不为空,发送注册失败信号,返回到do_child()函数
        connfd.send("FALL")
        return

    sql = "insert into user values ('%s','%s')"%(name,passwd)

    try:
        cursor.execute(sql)
        db.commit()
        connfd.send('OK')
    except:
        connfd.send("FALL")
        db.rollback()
        return
    else:
        print "注册成功 !"


def do_login(connfd,msg,db):
    print "登录中......."
    cursor = db.cursor() #创建游标
    s = msg.split(' ')
    name = s[1]
    passwd = s[2]

    try:
        sql = "select * from user where name = '%s' and passwd = '%s'"%(name,passwd)
        cursor.execute(sql)
        data = cursor.fetchone()
        print data
    except:
        pass

    if data == None:
        connfd.send("FALL")
    else:
        connfd.send('OK')

    return


def do_query(connfd,msg,db):
    print "in query......."
    cursor = db.cursor()
    s = msg.split(' ')
    word = s[1]
    name = s[2]

    try:
        f = open(DICT_TEXT,'r')
    except:
        print "open failed"
        connfd.send('FALL')
        return

    connfd.send('OK')
    sleep(0.1)
    while True:
        buf = f.readline()
        f.flush()

        if buf == '':
            connfd.send("not found")
            f.close()
            break

        temp = buf.split(' ')

        if temp[0] == word:

            msg = buf
            connfd.send(msg)

            insert_history(db,word,name)

            f.close()
            return


def do_history(connfd,msg,db):
    print "in history......."
    cursor = db.cursor()
    s = msg.split(' ')
    name = s[1]

    sql = "select * from hist where name = '%s'"%name

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        connfd.send('OK')
    except:
        print "history failed"
        db.rollback()
        connfd.send('FALL')

    for row in results:
        name = row[0]
        word = row[1]
        time = row[2]
        sleep(0.02)
        connfd.send("%s  %s  %s"%(name,word,time))

    sleep(0.1)
    connfd.send('over')
    return


def insert_history(db,word,name):
    time = ctime()
    cursor = db.cursor()
    sql = "insert into hist values('%s','%s','%s')"%(name,word,time)
    print sql
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print "sorry insert failed"
        db.rollback()
        return


def main():
    signal(SIGCHLD,SIG_IGN) #防止僵尸进程

    db = MySQLdb.connect('localhost','root','123','dict') #链接数据库

    HOST = sys.argv[1]
    PORT = int(sys.argv[2])

    sockfd = socket()                  #创建父进程套接字
    sockfd.bind((HOST,PORT))            #绑定地址与端口
    sockfd.listen(5)                    #监听

    while True:                        #使用死循环,用来一直接收新的子进程链接请求
        try:
            connfd,addr = sockfd.accept()
            print "链接成功,地址为: ",addr
        except KeyboardInterrupt:
            raise
        except:
            continue                   #发生异常时,返回重新接收链接请求

        pid =  os.fork()

        if pid < 0:
            print "create child process failed"
            connfd.close()
            continue
        elif pid == 0:  #子进程,用来和客户端进行交互
            sockfd.close()  #将父进程套接字关闭,
            do_child(connfd,db) #执行子继承,开始交互,将数据库和子进程套接字传参
        else:
            connfd.close()  #父进程,关闭子进程套接字,返回,继续进行接收
            continue
    #需要退出程序时,关闭数据库,关闭套接字,退出程序
    db.close()
    sockfd.close()
    sys.exit(0)


if __name__ == "__main__":
    main()
