#!usr/bin/python
#coding=utf-8
'''
10. 编写python程一个模块完成
：给定一个列表，将其从小到大排序，列表自己拟定用于排序方法的检测。
要求至少写出两种排序方法并且其中一种为快速排序方法，另一种任选。
'''
l=[44,5,76,43,8,1,9,4,10]
def select(l):
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                l[i],l[j]= l[j],l[i]
    print l
print "before:",l
print "after: ",
select(l)
