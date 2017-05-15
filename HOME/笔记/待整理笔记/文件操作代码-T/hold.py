#!/usr/bin/python
#coding=utf-8
with open('file','w') as f:
    f.write("我不好")
    f.seek(-9,1)       # NOTE:如果参数1如果是指针越过文件开头,则报错,如果为向后移动,超过了文件末尾,则指向文件末尾
    f.write('你好')
