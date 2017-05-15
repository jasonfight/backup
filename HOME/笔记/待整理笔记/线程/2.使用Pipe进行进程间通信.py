#!/usr/bin/python
#coding=utf-8
'''
使用Pipe() 进行进程间通信
执行结果:
父进程pid: 3627 ------- 子进程pid: 3628
父进程pid: 3627 ------- 子进程pid: 3630
父进程pid: 3627 ------- 子进程pid: 3631
父进程pid: 3627 ------- 子进程pid: 3629
父进程pid: 3627 ------- 子进程pid: 3633
父进程pid: 3627 ------- 子进程pid: 3635
父进程pid: 3627 ------- 子进程pid: 3634
父进程pid: 3627 ------- 子进程pid: 3632
父进程pid: 3627 ------- 子进程pid: 3636
父进程pid: 3627 ------- 子进程pid: 3637
hello0 3627
hello2 3627
hello3 3627
hello1 3627
hello5 3627
hello7 3627
hello6 3627
hello4 3627
hello8 3627
hello9 3627
'''
from multiprocessing import Process,Pipe
import time,os

process_list = []

read,write = Pipe()

def f(conn,name):
    time.sleep(1)
    conn.send('hello'+str(name))	#子进程,将'hello0-9'添加到管道中.
    print '父进程pid:',os.getppid(),'-------','子进程pid:',os.getpid()

if __name__ == "__main__":

    for i in range (10):
        p = Process(target = f,args = (write,i))
        p.start()
        process_list.append(p)
    for j in process_list:
        j.join()
    
    for i in range(10):		#将管道中的内容提取出来
        print read.recv(),os.getpid()


