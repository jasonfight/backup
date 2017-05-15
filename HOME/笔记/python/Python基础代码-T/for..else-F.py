#!/usr/bin/python
#coding=utf-8
'''
for...else...
在for语句执行完毕后,执行else语句
'''

for i in [1,2,3,4,5]:
    print "hi,%d"%i
    if i == 3:
        continue	#跳出该循环,执行下一次循环
	print '----'
else:
    print "gameover"

for i in range(1,50,2): #从1到49遍历.步长为2
    print i,
