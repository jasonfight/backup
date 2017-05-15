#!/usr/bin/python
#coding=utf-8
11. 编写python程序: 导入属性.假设你的模块 mymodule 里有一个 foo() 函数。

    1.把这个函数导入到你的名称空间有哪两种方法?
    2.这两种方法导入后的名称空间有什么不同?
答案:
第一种方法: import mymodule  调用该函数时,需要通过 mymodule.foo() 来调用
第二种方法: from mymodule import foo  调用该函数时,直接使用 foo() 来调用
第2题:
    使用 import mymodule 导入, foo()的命名空间仍在mymodule中,在调用时,应该使用
mymodule.foo() 来调用
    使用 from mymodule import foo 方法导入
foo()函数的命名空间为导入模块的本地空间, 调用该函数时,直接使用 foo() 来调用
