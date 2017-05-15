#!/usr/bin/python
#coding=utf-8


# NOTE: 可是用 r+   w  a  参数来进行write 操作   r+:写入的内容从源文件第一行开始覆盖,且原文件必须存在
# NOTE:  w  是直接覆盖整个文件    a  是在追加到原文件中
f = open('text.txt','a')
s = "天王盖地虎,宝塔镇河妖\n"

f.write(s)
