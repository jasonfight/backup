#!/usr/bin/python
# coding=utf-8
'''
在终端中输入字符串,将字符串重写入名称为参数一的文件中,当以#为一行输入时,结束本程序
'''

import sys

f = open(sys.argv[1],'w+')

while True:
    str = sys.stdin.readline()      # NOTE: 将终端的标准输入流的一行赋值给str
    if str == '#\n':                # NOTE: 当读取到该行只有一个#时,结束程序
        break
    f.write(str)

f.close()
