#!/usr/bin/python
'''
功能要求: 打印九九乘法表.
思路:1.两层循环,外层循环控制层数,行号从1到9
     2.内层循环控制列数,从1到行号,输出 列号*行号=结果
     3.每当每层循环结束一次后,进行换行

'''



for i in range(1,10):
    for j in range(1,i + 1):
        print "%d * %d = %-2d "%(j,i,i * j),
    print ""
