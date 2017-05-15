#!/usr/bin/python
#coding=utf-8

score=input("please input your score:")
if score>100 or score<0:
    print "please input correct score!"
    exit()
if score >= 90:
        print "your grade is A"
elif score >= 80:
        print "your grade is B"
elif score >= 70:
        print "your grade is C"
elif score >= 60:
        print "your grade is D"
else :
        print "your grade is Bad"
