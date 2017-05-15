#!/usr/bin/python
#coding=utf-8
'''
7. 编写python程序: 完成一个双色球彩票的数字生成过程，
其中前6个蓝色球数字范围为1-33的随机数，
最后一个红球数字为1-16的随机数。且前6个数不会重复。
使用random模块完成。得到这七个数后放到一个列表中打印，
打印要蓝球六个数按升序排列，红球放在最后。
思路:
1.先用一个死循环 生成六个不相同的蓝色的数,当个数为六个时,跳出循环,
2.将这六个数按照从大到小排序
3.生成一个红数,放到蓝数的后面

'''
import random
l=[]
num=0
while True:
    i = random.randint(1,33)
    if i not in l:
        l.append(i)
        num+=1
    if num == 6:
        break
# print l

for j in range(0,6):
    for n in range(0,j):
        # print 'j=',j
        # print 'l[%d]='%j,l[j]
        # print 'n=',n
        # print 'l[%d]='%n,l[n]
        if l[n]> l[j]:
            l[n],l[j] = l[j],l[n]
# print l
m = random.randint(1,16)
l.append(m)
print l
