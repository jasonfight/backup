#!/usr/bin/python
#coding=utf-8

'''
4. 运用python完成二分查找的代码
'''

l = [1,2,3,4,5,6,7,8,9]
def search(list,arg):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low +high) // 2
        if list[mid] < arg:
            low = mid +1
        elif list[mid] > arg:
            high = mid -1
        else:
            return mid
print '%d的位置为%d'%(4,search(l,4))
