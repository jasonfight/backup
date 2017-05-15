#!/usr/bin/python
#coding=utf-8
import random
i=0
while i<4:
    print "***********"
    num=input("input 0-9:")
    xnum=random.randint(0,9)

    x=3-i
    if num==xnum:
        print "you are right!"
        break
    elif num<xnum:
        print "smaller,the answer is %d,remain %d times"%(xnum,x)
    elif num>xnum:
        print "bigger,the answer is %d,remain %d times"%(xnum,x)
    print "--------------------------------------------"

    i += 1
