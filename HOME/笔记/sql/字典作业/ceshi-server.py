#!/usr/bin/python
#coding=utf-8
#!/bin/python
#coding=utf-8
import socket,traceback,os,sys,MySQLdb

def login(c,data):
    print 'login started'
    name = data[1]
    passwd = data[2]
    sql = 'select * from usr where name = "%s" and password = "%s"'%(name,passwd)
    cursor.execute(sql)
    data = cursor.fetchone()
    if not data:
        c.send('账号密码错误')
        return

    print name,passwd
    c.send('OK')
    print 'login over'
    while True:
        print '等待二级界面命令:'
        data = c.recv(1024)
        if data == 'S':
            while True:
                search(c)
        elif data == "H":
            print 'history.....'
        elif data == 'B':
            main()
        else:
            continue


def register(c,data):
    print 'register started'
    print '接收成功',data
    c.send('register OK')
    print 'regester over'

def search(c):
    print 'search started'
    f = open('dict.txt','r')
    print 'searching'
    while True:
        word = c.recv(1024)
        print '待查询词汇:',word
        f.seek(0,0)
        while True:
            line = f.readline()
            list1 = line.split(' ')

            if word == list1[0]:
                del list1[0]
                while list1[0] == "":
                    del list1[0]
                translation = ' '.join(list1)
                c.send(translation)
                break
            if line == "":
                c.send('查无此词')
                break
    print 'search over'
def main():
    while True:
        print '等待链接...'
        try:
            c,addr = s.accept()
        except:
            pass
        pid = os.fork()
        if pid:                # NOTE: 父进程,进行子进程的创建
            c.close()
            os.waitpid(-1,os.WNOHANG)
            continue
        else:                  # NOTE: 子进程,进行数据的操作
    	    s.close()
            try:
                print '链接成功'
                while True:
                    print '等待接收命令:'
                    data = c.recv(1024)
                    data1 = data.split(' ')

                    if data1[0] == "L":
                        while True:
                            print 'login start.....'
                            login(c,data1)
                    elif data1[0] == 'R':
                        print 'register starting.....'
                        register(c,data1)
                    else:
                        continue
            except (KeyboardInterrupt,SystemExit):
                raise
            except:
                traceback.print_exc()

            c.close()
            sys.exit(0)
if __name__ == '__main__':
    host = ''
    port = int(sys.argv[1])
    s = socket.socket()
    s.bind((host,port))
    s.listen(5)
    db = MySQLdb.connect('localhost','root','123','dict')
    cursor = db.cursor()
    main()
