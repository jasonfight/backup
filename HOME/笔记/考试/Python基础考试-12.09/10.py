#!/usr/bin/python
#coding=utf-8
'''
10. 编写python程一个函数: 其参数为一个字符串，函数删除字符串中的空格和‘-’，
在一个可以循环读取的程序中进行测试，直到用户输入空行，对于任何输入字符串，
函数都应该使用和并可以显示结果。

'''



def test(a):
    result=''
    for i in a:
        if i != ' ' and i != '-':
            result=result+i
    print result
while True:
    a=raw_input('请输入一个字符串:')
    if a == "":
        break
    test(a)
