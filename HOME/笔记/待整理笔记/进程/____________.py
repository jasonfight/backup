#!/usr/bin/python
#coding=utf-8

import multiprocessing,time,sys,subprocess

def a():
    p = multiprocessing.current_process()
    print 'starting:',p.name,p.pid
    sys.stdout.flush()
    time.sleep(1)
    print 'Exiting:',p.name,p.pid
    sys.stdout.flush()

def b():
    p = multiprocessing.current_process()
    print 'starting:',p.name,p.pid
    sys.stdout.flush()
    print 'Exiting:',p.name,p.pid
    sys.stdout.flush()

if __name__ =="__main__":
    d = multiprocessing.Process(name = 'a',target = a)
    d.daemon= True

    n = multiprocessing.Process(name = 'b',target = b)
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()
