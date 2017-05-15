#!/usr/bin/python
#coding=utf-8
'''
如果 assert后面的逻辑判断为假,则不继续执行 try 中的语句,直接被except 捕获并进行响应处理,
如果为真,怎继续执行程序.
'''
a = input()
try:
    assert a > 5       
    if a>5:
        print 'a>5'
    else:
        print 'a<5'
except AssertionError :
    print 'No assert error'
