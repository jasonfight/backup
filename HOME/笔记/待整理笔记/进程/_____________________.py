#!/usr/bin/python
#coding=utf-8
import sys,os
try:                         # NOTE: 将第一参数作为源文件以读写模式打开
    fd_src = open(sys.argv[1],'r+')
except:
    print "open fd_src failed"

fd_src.seek(0,2)            # NOTE:将指针指到文件末尾
size = fd_src.tell()       # NOTE: 将文件末尾的指针位置赋值给size,size即为文件的总大小


try:                          # NOTE: 将第二参数作为目标文件以读写模式创建并打开
    fd_dst = open(sys.argv[2],'w+')
except:
    print "open fd_dst failed"

size /= 2

pid = os.fork()

if pid < 0:
    print "fail to fork"
    exit(-1)
elif pid == 0:         #子进程,用来复制文件的后半部分
    pass
    fd_src.close()        #将两个文件重新打开,游标调整到文件的中间
    fd_dst.close()
    fd_src = open(sys.argv[1],'r+')
    fd_dst = open(sys.argv[2],'w+')
    fd_src.seek(size,0)
    fd_dst.seek(size,0)

    while True:
        buf = fd_src.readline()
        if buf == '':
            break
        fd_dst.write(buf)
    exit(0)

else:                                  #父进程,用来复制文件的前半部分
    num = 0
    fd_src.seek(0,0)
    fd_dst.seek(0,0)
    print  'siza:',size
    while True:
        buf = fd_src.readline(1)
        num += len(buf)
        if num <= size:
            fd_dst.write(buf)
        else:
            break
    os.wait()
    exit(0)
