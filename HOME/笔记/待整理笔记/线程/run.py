#!/usr/bin/python
#coding=utf-8
'''
自己创建一个进程
'''



import multiprocessing,time

class ClockProcess(multiprocessing.Process):
    def __init__(self,value):
        multiprocessing.Process.__init__(self)
        self.value = value
    def run(self):
        n = 4
        while n >0 :
            print time.ctime()
            time.sleep(1)
            n -= 1

p = ClockProcess(2)
p.start()       # NOTE:自动调用 run函数,该run函数为multiprocessing中Process类里原有的函数,在此模块中覆盖它,达到重新设计进程的目的
while True:
    time.sleep(1)
    print "222222"
