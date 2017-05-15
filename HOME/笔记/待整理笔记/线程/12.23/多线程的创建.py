#!/usr/bin/python
#coding=utf-8

from time import ctime,sleep
import os,threading

def music(name):
    print 'music..',name,ctime()
    print os.getpid()
    sleep(2)
def movie(name):
    print 'music..',name,ctime()
    print os.getpid()
    sleep(4)
def player(name):
    r = name.split('.')[1]
    if r == 'mp3':
        music(name)
    elif r == 'mp4':
        movie(name)
    else:
        print '播放错误'
l= ['我要你.mp3','驴得水.mp4']
threads = []
files = range(len(l))
for i in files:
    t = threading.Thread(target = player,args = (l[i],))
    threads.append(t)
if __name__ == "__main__":
    for i in files:
        threads[i].start()
    for i in files:
        t.join()
    print "all over",ctime()
