#!/usr/bin/python
#coding=utf-8

'''
7.使用fork创建新的进程，
并且列举出防止僵尸进程的方法。（至少两种）
'''
import signal,os,sys,time

pid = os.fork()
if pid < 0:
    print 'error'
if pid == 0:
    print '一级子进程创建成功',os.getpid()
    son_pid = os.fork()
    if son_pid < 0:
        print 'eror'
    elif son_pid == 0:
        print '二级子进程创建完成',os.getpid()
        while True:
            pass
    elif son_pid > 0:
        print '关闭一级子进程',os.getpid()
        sys.exit()
if pid > 0:
    time.sleep(0.1)
    os.waitpid(-1,os.WNOHANG)
    print '父进程',os.getpid()
    while True:
        pass

# 防止僵尸进程的方法:
#1.创建二级子进程,将一级子进程结束
#2.使用os.waitpid(os.WNOHANG)方法来防止僵尸进程
