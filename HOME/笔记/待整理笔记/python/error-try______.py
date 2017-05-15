#!/usr/bin/python
#coding=utf-8
'''
try...except...语句:
用法:
当try中的语句出现错误时,停止继续执行try语句,跳入except语句进行异常捕捉,匹配响应的异常类型
然后进行相应的处理.
如果没有出现异常,则会执行else语句,
finally语句在最后执行,无论发生异常与否,都会执行.
一个except语句可以捕获多个异常类型,不同的类型要在一个小括号中,并且使用逗号隔开
语法:
try:
    语句块1
except (TypeError1,TypeError2):
    语句块2
else:
    语句块三
finally:
    语句块四

div(3,0) 时,执行结果:

0 can not be division
finally.....
test over

div(3,'a') 时,执行结果:

str can not be division
finally.....
test over

div(3,1) 时,执行结果:

3
else.....
finally.....
test over
'''
def div(a,b):
    try:
        c = a / b           # NOTE: 当该行语句为异常时,后面的语句就不会执行,会跳转到except语句
        print c
    except TypeError:
        print "str can not be division"
    except (ZeroDivisionError,ValueError):  # NOTE: 如果异常为except后指定异常,执行except语句并继续执行整个程序,否则不执行.直接跳出程序
        print '0 can not be division'
    except:                 # NOTE: 为其他异常时,不采取操作,继续执行程序
        pass
    else:               # NOTE: 没有发生异常时,执行else语句
        print "else....."
    finally:
        print 'finally.....' # NOTE: 无论有没有异常,均执行该语句.
div(3,1)

print 'test over'
