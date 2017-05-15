#!/usr/bin/python


a=int(raw_input("please input a:"))
b=int(raw_input("please input b:"))
c=int(raw_input("please input c:"))
s=(a+b+c)/2
if a+b>c and a+c>b and b+c>a:
    import math
    area=int(math.sqrt(s*(s-a)*(s-b)*(s-c)))
    print "area is ",area
else:
    print "please input correct num!"
