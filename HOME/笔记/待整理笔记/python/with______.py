#!/usr/bin/python
#coding=utf-8
'''
with...as...语句:
语法:
with 类名 as 变量名:
    语句块

执行完语句块后,变量名及类名会自动销毁
在使用with...as...语句之前,需要将类提前创建,并且将__enter__,__del__,__exit__几个魔法方法
定义好.格式都是代码中的固定格式,语句块一般为pass


用来创建一个对象
在执行with语句中,相当于创建了一个对象
执行顺序如下:
先执行__enter__中的语句
再执行 with中的语句
再执行__del__的语句
最后执行 __exit__的语句

语法:
with 类名 as 变量名:
    语句块
执行完语句块后,变量名及类名会自动销毁

指定结果:
1.enter...
2.doing something
4.exit...
3.del...
5.over


'''
class Test(object):

    def __enter__(self):
        print '1.enter...'
    def __del__(self):
        print '3.del...'
    def __exit__(self,type,value,traceback):
        print '4.exit...'

with Test() as Thing:
    print '2.doing something'

print '5.over'
