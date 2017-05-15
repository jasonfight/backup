#!/usr/bin/python

def decorator(func):
    def back():
        return func() + "decorator test"
    return back

@decorator   ###====> F = decorator(F)
def F():
    return "This is a func"

print F()
