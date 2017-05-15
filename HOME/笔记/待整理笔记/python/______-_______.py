#!/usr/bin/python
#coding=utf-8

def fun_out():
a = 4
	def fun_in():
    		nonlocal a             # NOTE: 需要更改外层函数变量时,需要加nolocal加以声明,用法与函数引用全局变量时的global一致
   		a+=2
   		print ("in=",a)

fun_in()

print ("out=",a)

fun_out()
