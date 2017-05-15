#!/usr/bin/python
#coding=utf-8

class Singleton(object):
    # a =1
    def __new__ (cls,*args,**kw):
        if not hasattr(cls,'_instance'): #判断cls中,有没有_instance对象,如果有,返回True
            orgi = super(Singleton,cls)
            cls._instance = orgi.__new__(cls,*args,**kw)
        return cls._instance

class MyClass(Singleton):
    a =1

one = MyClass()         #创建one时,Singleton没有_iinstance的对象,执行 __new__中的if语句,
                        #为myclass()的对象创建_instance对象,此时one与_instance等价
two = MyClass()         #one 和two 等价
# one = Singleton()
# two = Singleton()

print id(one)
print id(two)

one.a = 3
print one.a
print two.a
