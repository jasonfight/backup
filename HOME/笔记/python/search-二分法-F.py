#!/usr/bin/python



'''
二分法查找
'''
def BinSearch(array,t):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] < t:
            low = mid + 1
        elif array[mid] > t:
            high = mid - 1
        else:
            return mid

    return -1

l = [1,2,3,4,5,6,7,8]

print(BinSearch(l,3))
