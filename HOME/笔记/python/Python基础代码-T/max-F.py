#!/usr/bin/python
#coding=utf-8

'''
鞍点的寻找.
思路:将每一行的最大数找出来,然后将最大数与其所在列的所有数比较,如果还是最大,则为鞍点
进行输出
'''
l = [[5,3,8,6],
     [4,7,2,9],
     [3,1,6,4]]

for i in range(3):
    line_max = max(l[i])
    k = l[i].index(line_max)
    num = l[i][k]
    for j in range(3):
        if l[j][k] > num:
            num = l[j][k]
    if num == line_max:
        print "l[%d][%d] = %d"%(i,k,num)

