#!/usr/bin/python
#coding=utf-8

'''

创建进程的两种方法:
(两种方法的代码会有干扰,不能直接执行整个模块的代码,测试时需将其他代码注释,只执行一种代码)

1.使用os模块创建进程:
你能在POSIX系统上使用,window系统中,使用多线程变成来完成并发任务
'''


import os,time
a = os.fork()
if a < 0:
    print '创建进程失败'
elif a == 0:
    print "创建子进程成功,子进程PID为%s"%os.getpid()       #--->子进程的PID
    print "父进程的PID为%s"%os.getppid()                 #--->父进程的PID
    print "----"
    time.sleep(1)
if a > 0:
    os.wait()   #阻塞函数,当子进程结束后才冲破阻塞
    print '创建父进程成功,父进程PID为%s'%os.getpid()  #---->父进程的PID


'''
使用multiprocessing 模块中的Process类来创建进程,并使用join()函数防止僵尸进程的出现
先创建函数,每一个函数可以通过Process调用来成为一个进程,函数的参数通过Process的args参数进行传参
进程的创建:
p = multiprocessing.Process(target = 函数名, name = '进程名',args=(参数元组))
p.start()
'''
import multiprocessing
import os
def son():
    print '子进程创建成功,PID为:%s'%os.getpid()
    return
l = []

print '父进程PID为:%s'%os.getpid()
for i in range(3):              #创建3个子进程
    a = multiprocessing.Process(target = son)
    a.start()
    l.append(a)
for a in l:
    a.join()        #回收子进程的退出,防止僵尸进程的产生
