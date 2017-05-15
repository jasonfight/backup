#!/usr/bin/python
#coding=utf-8

import getpass,smtplib
from smtplib import SMTP as smtp

mail_host = 'smtp.126.com'
mail_user = 'guohao0221@126.com'
# mail_pass = getpass.getpass()
mail_pass = 'Skying'
sender = 'guohao0221@126.com'
receiver = ['18342964755@163.com']

message = '''From:guohao0221@126.com\r\nTo:18342964755@163.com\r\nSbject:test
msg\r\n\r\nPython test email '''
print message
try:
    smtpobj = smtp(mail_host)
    smtpobj.login(mail_user,mail_pass)
    # smtpobj.sendmail(sender,receiver,message)
    print 'ok'
except smtplib.SMTPException,e:
    print 'error',e
