#!/usr/bin/python

from ftplib import FTP


f = FTP('ftp.ibiblio.org')

print "Welcome:",f.getwelcome()

f.login()

print "PWD:",f.pwd()
print "dir:",f.dir()

f.quit()

