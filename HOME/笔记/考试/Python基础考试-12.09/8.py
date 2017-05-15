#!/usr/bin/python
#coding=utf-8
'''
8. 编写python程序: 求一个矩形方阵中的鞍点。在一个方阵中，
如果一个数在它所在的行和列中都是最大的数，那么称这个数为矩阵中的一个鞍点。
使用列表的嵌套，自己设计一个3行4列的矩阵，
求出其中鞍点
思路:
1.先求出每一行中最大的数,然后确定其行位置和列位置, i为行号,j为列号
将每一行的最大数跟其同一列的所有数比较,如果该数还是最大,则输出该数

'''
l=[[1,2,5,4],
   [3,4,5,6],
   [7,5,6,3]]
for i in range(3):
    #  print l[i]
     maxnum=max(l[i])
    #  print maxnum
     k=l[i].index(maxnum)
    #  print k
     result=maxnum
     for j in range(3):
        if maxnum < l[j][k]:
             maxnum = l[j][k]
    #  print 'maxnum=',maxnum
    #  print 'result=',result
     if maxnum == result:
         print maxnum
