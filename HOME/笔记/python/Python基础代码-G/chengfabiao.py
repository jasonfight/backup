#!/usr/bin/python
#coding

for i in range(1,10):
    for j in range(1,i+1):
        s=i*j
        #print j,'*',i,'=',s," ",
        print "%d*%d=%d"%(j,i,s),
    print ""
