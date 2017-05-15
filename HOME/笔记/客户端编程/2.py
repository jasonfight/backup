#!/usr/bin/python
#coding=utf-8
import ftplib,os,socket
HOST = 'ftp.kernel.org'
DIRN = 'pub/linux/kernel'
FILE = 'README'
def main():
    f = ftplib.FTP(HOST)
    print 'connected to host',HOST

    f.login()
    print 'logged in as "anonymous"'

    f.cwd(DIRN)
    print 'change to "%s" folder'%DIRN

    f.retrbinary('RETR %s'%FILE,open(FILE,"wb").write)
    print  ' download "%s" to cwd'%FILE

main()
