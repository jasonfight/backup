#!/usr/bin/python
#coding=utf-8

'''
y有错误,带改正
'''
from time import sleep
import multiprocessing
import sys

def woker_with(lock,stream):
    with lock:
        for i in range(5):
            sleep(1)
            stream.write('lock with')
def woker_no_with(lock,stream):
    lock.acquire()
    try:
        for i in range(5):
            sleep(1)
            stream.write('lock acquire')
    finally:
        lock.release()
lock = multiprocessing.lock()
w = multiprocessing.Process(target = woker_with,args = (lock,sys.stdout))
nw = multiprocessing.Process(target  = woker_no_with,args = (lock,sys,stdout))

w.start()
nw.start()
w.join()
nw.join()
