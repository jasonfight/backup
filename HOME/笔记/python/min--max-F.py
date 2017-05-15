#!/usr/bin/python
#coding=Utf-8

'''
排序法:
'''
l=[44,5,76,43,8,1,9,4,10]


def bouble (l):
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    print l


'''
选择排序法:
算法:

'''

def select(l):
    for i in range(len(l)-1):
        minnum = i
        for j in range(i+1,len(l)):
            if l[minnum]>l[j]:
                minnum = j
        if minnum != i:
            l[minnum],l[i]= l[i],l[minnum]
    print l
'''
选择排序法:
算法:
从第一数个开始,后面的数如果有小于该数的,就将两个数交换,直到该数后面没有小于该数的数
在从第二个数开始,将第二个数后面小于第二个数的数都放在第二个数的前面,
一直循环到最后一个数
思路:
使用两个循环,外循环 i 控制待比较数的位置,从 
'''

def select2(l):
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                l[i],l[j]= l[j],l[i]
    print l
'''
插入排序法:
算法:
从第一个开始往右找,一直找到最后一个.先将该位置的数赋值给一个第三方变量key,
然后从该位置往左遍历,逐个与key进行比较,如果大于等于key,
就将前面的数赋值给后面的数,直到遍历到最左面或者小于key
将key值重新赋值给遍历循环的位置.

思路:
使用两个循环,
外循环 i 控制从第一位置遍历到最后一位置,将i赋值给第三方变量 key.
内循环 j 控制比较的方式,以外循环遍历到的位置 i 为起点,
再往前遍历,找到 j-1 位置的值比 key 大的数,赋值给 j 位置 
直到 j=0 或者 j-1 位置的数 小于 key ,然后将 key 赋值给 j 位置 


'''

def insertion_sort(L):
    for i in range(len(l)):
        key = l[i]
        j = i
        while j > 0 and l[j - 1] >= key:
            l[j] = l[j - 1]
            j -= 1
        l[j] = key
    print "insertion",l

print l
bouble(l)
select(l)
select2(l)
insertion_sort(l)
'''
快速排序法思路:
将第一位的下标定义为low,最后一位的下标定义为high位,将low位赋值给key,
在整个数列中从右往左移动high,找到小于等于key数,赋值给low位,
然后将low从做往右移动,找到第一个大于等于key的数,赋值给high位,然后将key赋值给low位
记录low的下标为p
将p+1为low 和 p-1 为high 分别在进行上面的操作,直到 low=high
'''




l=[44,5,76,43,8,1,9,4,10]





def parttion(l, left, right):
    key = l[left]
    low = left
    high = right

    while low < high:

        while (low < high) and (l[high] >= key):
            high -= 1

        l[low] = l[high]

        while (low < high) and (l[low] <= key):
            low += 1

        l[high] = l[low]
        l[low] = key
    return low

def quicksort(l, left, right):
    if left < right:
        p = parttion(l, left, right)
        quicksort(l, left, p-1)
        quicksort(l, p+1, right)
    return l
print "before sort:",l

l1 = quicksort(l, left = 0, right = len(l) - 1)
print "after sort:",l1


