#!/usr/bin/python
#coding=utf-8
'''
continue与break的用法:
continue:结束本次循环,跳如下次循环
break: 结束所在循环.

'''



i = 0
while i < 10:
    i += 1
    if i < 5:
#        break
        continue
    print i
#else:
#    print "+++++++++++++++"
