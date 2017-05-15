#!/usr/bin/python

class Person(object):

    print "class ....."

    def __init__(self):
        print "init...."

    def __new__(cls):
        print "new ......"
        return object.__new__(cls)

    def color(self):
        print "color....."

    def __del__(self):
        print "del....."


Lilei = Person()
print "1---------------"

Lilei.color()
print "2---------------"

Hanmei = Person()
print "3---------------"
Hanmei.color()
