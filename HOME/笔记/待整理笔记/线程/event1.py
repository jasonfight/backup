#!/usr/bin/python
#coding=utf-8


import threading
from time import sleep

e = threading.Event()

e.set()		#更改事件为设置状态

event = e.wait() #将事件的设置状态赋值给event
print(event)

e.clear()	#清除设置状态

event = e.wait(3)	#阻塞3秒,如果事件没有被设置,则冲破阻塞,将事件状态赋值给event

print("timeout:",event)


