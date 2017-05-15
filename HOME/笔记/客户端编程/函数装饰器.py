#!/usr/bin/python
#coding=utf-8

def decorator(func):
    def back():
        return func() + 'decorator test'
    return back

@decorator  #---->F = docorator(F)
def F():
    return 'this is a func '


print F()
# print decorator(F)
