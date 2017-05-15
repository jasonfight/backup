#!/usr/bin/python
#coding=utf-8
'''
将1-10的数列按照奇数在前,偶数在后排列
将 2,9 互换,4,7 互换即可.即将1,8位置互换,3,6位置互换


'''

def fun(l):
    i = 0
    j = len(l)-1
    
    while i < j-3:
        while l[i] % 2 != 0: #为奇数,位置向后移动一个
            i += 1
        while l[j] % 2 == 0: #为偶数,位置向前移动一个
            j -= 1
        print 'l[%d]=%d,l[%d]=%d'%(i,l[i],j,l[j])

        l[i],l[j] = l[j],l[i]

l = [1,2,3,4,5,6,7,8,9,10]
print "before:",l

fun(l)
print "after:",l
