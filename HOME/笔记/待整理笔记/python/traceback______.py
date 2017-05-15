#!/usr/bin/python
#coding=utf-8


'''
引入 traceback 模块 来显示异常代码的所在行数及异常信息
用法:
首先 使用import traceback 引入 tracemback 模块
使用时,在except 语句块中添加:
    traceback.print_exc()

执行结果:
0 can not be division
integer division or modulo by zero
Traceback (most recent call last):
  File "try1.py", line 13, in div
    return a / b
ZeroDivisionError: integer division or modulo by zero
finally.....
test over

'''
import traceback

def div(a,b):
    try:
        return a / b
    except (ZeroDivisionError,TypeError),g: # NOTE: 也可将逗号换成as,python3 中使用as
        print '0 can not be division'
        print g      # NOTE: 输出错误类型的说明文档
        traceback.print_exc()                # NOTE: 输出错误所在行及错误信息.
    else:
        print "else....."
    finally:
        print 'finally.....'
div(3,0)
print 'test over'
