#!/usr/bin/python

def fun(char):
    l = char.split(' ')
    char = ''.join(l)
    l = char.split('-')
    char = ''.join(l)
    
    return char



while True:
    s = raw_input()
    if not len(s):
        break

    print "before :",s

    s = fun(s)

    print "after:",s
