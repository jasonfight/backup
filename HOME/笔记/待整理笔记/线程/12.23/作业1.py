#!/usr/bin/python
#coding=utf-8

'''
为什么输出两遍
'''

from time import ctime,sleep
import os,threading

def player(file,time):
    for i in range(2):
        print "playing:",file,ctime()
        sleep(time)

l = {'我要你.mp3':3,'驴得水.mp4':5,'you and i':4}
threads = []
files = range(len(l))

for file,time in l.items():
    t = threading.Thread(target = player,args = (file,time))
    threads.append(t)

if __name__ == "__main__":
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()
    print "all over",ctime()
