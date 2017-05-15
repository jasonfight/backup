#!/usr/bin/python
#coding=utf-8
'''

__call__   魔法方法,在类中添加该方法,相当于将方法名字命名为call,在调用时使用 a.call()

下面代码与上面代码等价:
class A(object):
    def call(self,x):
        print 'x:',x
a=A()
a.call(200)  # 需要加方法名称

输出结果:
x:200

'''


class A(object):
    def __call__(self,x):
        print 'x:',x
a=A()
a(200)		# 不需要加方法名称


'''
__call__   魔法方法,在类中添加该方法,相当于将方法名字命名为call,在调用时使用 a.call()

下面代码与上面代码等价:
class A(object):
    def call(self,x):
        print 'x:',x
a=A()
a.call(200)  # 需要加方法名称


'''
