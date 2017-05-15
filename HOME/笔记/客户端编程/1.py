#!/usr/bin/python
#coding=utf-8
from ftplib import FTP
f = FTP('ftp.ibiblio.org')
# f = FTP('0.0.0.0')
print 'welcome',FTP.getwelcome()    #获得欢迎界面
f.login()
print 'PWD',f.pwd() #获取当前目录
print 'dir',f.dir() #获取当前所在文件夹

f.quit()
