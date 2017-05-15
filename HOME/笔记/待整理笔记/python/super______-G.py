#!/usr/bin/python
#coding=utf-8
'''
子类方法与父类同名,又需调用父类函数时,使用super函数
语法:super(子类类名,self).父类方法名
输出结果为:
DiaoChan is a girl,she is about 160,and her breast is 90
DiaoChan is about 160
第一行的结果为子类本身的 about 方法输出的内容,
第二行的结果为引用父类的 about 方法输出的内容


'''


class Person(object):
    def __init__(self):
        self.height = 160

    def about(self,name):
        print("{} is about {}".format(name,self.height))

class Girl(Person):
    def __init__(self):
        super(Girl,self).__init__()     # NOTE:  子类方法与父类同名,又需调用父类函数时,使用super函数
        self.breast = 90
    def about(self,name):
        print("{} is a girl,she is about {},and her breast is {}".format(name,self.height,self.breast))
        super(Girl,self).about(name)

if __name__ == '__main__':
    Chan = Girl()
    Chan.about("DiaoChan")
