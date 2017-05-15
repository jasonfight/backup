#!/usr/bin/python
#coding=utf-8
for i in [1,2,3,4,5]:
    print 'i+4 \n %d'%i
print ""

for j in (1,2,3,):
    print j
print ""

for z in {1,2,4,}:
    print z
print ""

for x in 'hello':
    print x
print ""

for m in {'a':1,'b':2}:
    print m
print ""

d={'a':1,'b':2}
for n in d:
    print n,':',d[n]

for i in [1,2,3,4]:
    print i
else :            #else 可以和for配合使用,一般在执行完for后会执行else语句,
                 #只有在for中添加终止循环的语句(exit(),break)时,else才可能不执行.
    print "over"
#计算1-100的加和:
sum=0
for i in range(1,101):
    sum+=i
print sum
for (i,j) in [[1,2],[3,4]]:
    print i,j
