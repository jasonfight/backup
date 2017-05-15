#!/usr/bin/python

import smtplib
from smtplib import SMTP as smtp 
import getpass

mail_host = "smtp.126.com"
mail_user = "lvze_work@126.com"
mail_pass = getpass.getpass()

sender = "lvze_work@126.com"
receiver = ['guohao0221@126.com']

message = '''From:lvze_work@126.com\r\nTo:guohao0221@126.com\r\nSubject:test
msg\r\n\r\nPython email test'''

print message

try:
    smtpobj = smtp(mail_host)
    smtpobj.login(mail_user,mail_pass)
    smtpobj.sendmail(sender,receiver,message)
    print "OK"
except smtplib.SMTPException,e:
    print "error:",e
