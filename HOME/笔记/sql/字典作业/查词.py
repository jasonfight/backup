#!/usr/bin/python
# coding=utf-8
import time
# def query(arg):
#    while True:
f = open('dict.txt','r')
while True:
    data =raw_input("请输入单词:")
    while True:
        x = f.readline()
        m = x.split(' ')

        if data == m[0]:
            del m[0]
            while m[0] == "":
                del m[0]
            translation = ' '.join(m)
            print translation
            break
        if x == "":
            print '查无此词'
            break
