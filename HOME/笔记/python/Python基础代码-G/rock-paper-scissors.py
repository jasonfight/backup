#!/usr/bin/python
#coding=utf-8
import random
dic={'石头':0,'剪刀':1,'布':2}
while True :
    human=raw_input("请输入'石头','剪刀'或者'布':")
    print "human:",human
    robot=random.randint(0,2)
    l=['石头','剪刀','布']
    print "robot:",l[robot]

    if dic[human]==0:
        if robot==0:
            print "平局"
        elif robot==1:
            print "你赢了"
        elif robot==2:
            print "你输了"

    if dic[human]==1:
        if robot==1:
            print "平局"
        elif robot==2:
            print "你赢了"
        elif robot==0:
            print "你输了"

    if dic[human]==2:
        if robot==2:
            print "平局"
        elif robot==0:
            print "你赢了"
        elif robot==1:
            print "你输了"
