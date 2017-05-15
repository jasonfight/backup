#!/usr/bin/python
#conding=utf-8
a=int(raw_input("please input side a:"))
b=int(raw_input("please input side b:"))
c=int(raw_input("please input side c:"))
print "side a is:",a
print "side b is:",b
print "side c is:",c
if a+b>c and a+c>b and b+c>a:
    s=(a+b+c) / 2
    import math
    area=int(math.sqrt(s*(s-a)*(s-b)*(s-c)))
    print "the area is:",area
else:
    print "please input correct length of three sides! the sum of any two side'lehgth must longer than the third one!"
