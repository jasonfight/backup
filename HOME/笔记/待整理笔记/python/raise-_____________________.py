#!/usr/bin/python
#coding=utf-8


'''
raise 语句:
作用:自定义异常:
用法:
先创建一个错误类名,继承于Exception,
在执行过程中,如果执行了raise语句,不再继续执行try语句,直接跳入except语句进行错误捕捉
as 语句 是给 错误类型去一个别名,在后面的执行过程中,就可以使用别名来代表raise语句中自定义
错误类名后跟的参数

执行结果:
A
----------
自定义错误

'''

class MyError(Exception):
    pass

try:
    s = None
    if s is None:
        print 'A'
        raise MyError('自定义错误')
    print len(s)                # NOTE:  如果执行,则会报错,因为NoneType没有长度,不能使用len函数
except MyError as x :
    print '----------'
    print x
