#!usr/bin/python
#coding=utf-8
#求矩阵中的最大数,
l=[[1,2,3,4],
   [5,6,7,9],
   [1,7,10,2]]
max=l[0][0]
x=0
y=0
for i in range(3):
    for j in range(4):
        if l[i][j]>max:
            max=l[i][j]
            x=i;y=j
print "l[%d][%d]=%d"%(x,y,max)
