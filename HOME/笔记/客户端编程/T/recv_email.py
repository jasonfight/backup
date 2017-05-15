#!/usr/bin/python

from poplib import POP3
import getpass

p = POP3('pop.163.com')
p.user("sisuo321@163.com")
pwd = getpass.getpass()
p.pass_(pwd)

msg_ct,mbox_size = p.stat()

rsp,msg,siz = p.retr(msg_ct)

print rsp,siz

for eachLine in msg:
    print eachLine
