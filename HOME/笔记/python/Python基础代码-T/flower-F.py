#!/usr/bin/python
#coding=utf-8
'''
水仙花数:百位,十位,个位上的数的立方之和,如果等于数字本身,则为水仙花数
思路:
用一个循环将i从100到1000遍历
个位为 i 对 10 求余的结果
十位为 i 除以 10  然后对 10 求余的结果
百位为 i 对 100 求余的结果

将 求出来的三个数进行立方并加和 与原数进行比较,如果相等,则输出

'''

for i in range(100,1000):
    ge = i % 10
    shi = i / 10 % 10
    bai = i / 100

    if i == ge ** 3 + shi ** 3 + bai ** 3:
        print "%d "%i,

print ""
