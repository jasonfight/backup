#!/usr/bin/python
#/coding=utf-8

'''
避免僵尸进程的第二种方法:
在子进程1中再建立一个子进程2,然后将子进程1关闭
此时,子进程2成为孤儿进程,被init进程收养,子进程1结束,不会产生僵尸进程
'''

import os,time,sys


pid = os.fork()

if pid < 0:
    print "create process error"
elif pid == 0:
    pid = os.fork()

    if pid < 0:
        print "create process error"
    elif pid == 0:
        while True:
            time.sleep(1)
            print "子进程2",os.getpid()
    else:
        print "子进程1:",os.getpid()
        sys.exit()
else:
    os.wait()
    while True:
        time.sleep(1)
        print "父进程:",os.getpid()
