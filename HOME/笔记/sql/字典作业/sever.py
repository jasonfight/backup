#!/usr/bin/python
#coding=utf-8
#!/bin/python
#coding=utf-8
import socket,traceback,os,sys,MySQLdb

def login(c,data):
    c.send('OK')

    search(c)

def register(c,data):
    print 'started'
    data = c.recv(1024)
    print data
    c.send('register OK')
def quit():
    c.close()
def search(c):
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

def main():
    while True:
        print '等待链接...'
        try:
            c,addr = s.accept()
            print '222'
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()
            continue

        pid = os.fork()
        if pid:                # NOTE: 父进程,进行子进程的创建
            c.close()
            os.waitpid(-1,os.WNOHANG)
            continue

        else:                  # NOTE: 子进程,进行数据的操作
    	    s.close()
            try:
                while True:
                    data = c.recv(1024)
                    print data
                    data1 = data.split(' ')

                    if data1[0] == "L":
                        print 'login start.....'
                        login(c,data)
                    elif data1[0] == 'R':
                        print 'register starting.....'
                        register(c,data)
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
    qu = 0
    main()
