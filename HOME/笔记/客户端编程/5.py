#!/usr/bin/python
#coding=utf-8
from poplib import POP3 as pop3
import getpass

p =pop3('pop.126.com')
p.user('guohao0221@126.com')
pwd = getpass.getpass()
p.pass_(pwd)

msg_ct,mbox_size = p.stat()
rsp,msg,siz = p.retr(msg_ct)
print rsp,siz
for eachline in msg:
    print eachline
