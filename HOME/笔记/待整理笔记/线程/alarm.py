#!/usr/bin/python
#coding=utf-8
'''
执行结果:
2
wait.....
wait.....
wait.....
闹钟

'''


import signal,time

signal.alarm(5)   # NOTE:   5秒后发送种植信号
time.sleep(3)
num = signal.alarm(4)    # NOTE:覆盖上一个时钟的时间    返回值为上一个时钟的剩余时间
print num

while True:
    time.sleep(1)
    print "wait....."
