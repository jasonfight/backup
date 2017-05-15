#!/usr/bin/python


i = 3
while i >= 0:
    j = 0
    while j < i:
        print " ",
        j+=1
    j = 0
    while j < 7 - 2 * i:
        print "*",
        j+=1
    print ""
    i -= 1

i = 1
while i <= 3:
    j = 0
    while j < i:
        print " ",
        j+=1
    j = 0
    while j < 7 - 2 * i:
        print "*",
        j+=1
    print ""
    i += 1
