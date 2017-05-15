#!/usr/bin/python

def fun_out():
    a = 4
    def fun_in():
        nonlocal a
        a += 1
    fun_in()
    print (a)

fun_out()
