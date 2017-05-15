#!/usr/bin/python
#coding=utf-8
import sys
f=open(sys.argv[1],'a')
while True:
    line = sys.stdin.readline()
    if line == "#\n":
        break
    f.write(line)
f.close()
