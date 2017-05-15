#!/usr/bin/python
#coding=utf-8
import sys
before = open(sys.argv[1],'r')
after = open(sys.argv[2],'w')

while True:
    line = before.readline()
    after.write(line)
    if line == "":
        break
before.close()
after.close()
