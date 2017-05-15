#!/usr/bin/python
#coding=utf-8
'''
#质数

如果从2到一个数的开方,都不能整除这个数,则这个数就没有其他因子
质数是除了1和自身,没有因子的数
'''
import math

flag = 1
for num in range(2,100):
	for i in range(2,int(math.sqrt(num))):
		if num % i == 0:
			flag = 0
			break
		else:
			flag = 1
	
	if flag == 1:
		print "%d"%num
