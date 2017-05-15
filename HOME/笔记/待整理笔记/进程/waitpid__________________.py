#!/usr/bin/python
#coding=utf-8
'''
os.waitpid():
功能:处理子进程的信号,防止产生僵尸进程.
返回一个元组,为子进程的信号,第一个元素为子进程的PID,
os.waitpid()有两个参数
参数一:
-1,任何一个子进程退出,进行接收,
0:进程组中任意一个进程结束,进行接收,
大于0的任何数:接收特定PID的进程的退出
参数二:os.WNOHANG:判断子进程是否退出.如果退出,则进行处理,如果没有退出,
则不进行阻塞,同时执行后面的语句.
'''

import os,time

pid = os.fork() #=====>0
if pid < 0:
    print "create process failed"
elif pid == 0:               # NOTE: 当pid == 0 时,为子进程,子进程会复制所有父进程的执行结果,但不会继续执行
    print "Son process.....",os.getpid()
    print os.getpid()        # NOTE: 打印父进程的PID
    exit('------------')            # NOTE: 退出并打印括号中的内容
else:               # NOTE:  父进程
    time.sleep(0.1)
    print os.waitpid(-1,os.WNOHANG)   # NOTE:接收并打印子进程的信号,防止出现僵尸进程
    print "Parent process...",os.getpid()
    print pid                   # NOTE: 打印os.fork()函数的返回值,为子进程的PID
    while True:                 # NOTE: 函数会阻塞在此位置,不会执行后面的语句
        pass

print "+++++++++++++++++++"
