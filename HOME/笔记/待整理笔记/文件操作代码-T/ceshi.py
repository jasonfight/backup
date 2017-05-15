#!/usr/bin/python
#coding=utf-8

import time

s=time.localtime()
print s
print "%4d-%02d-%02d %d:%02d:%02d"%(s.tm_year,s.tm_mon,s.tm_mday,s.tm_hour,s.tm_min,s.tm_sec)
