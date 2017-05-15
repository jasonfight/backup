#!/bin/bash

if [ $# -ne 1 ]
then
  echo "输入有误"
  exit 1
fi                        #检测命令后是否跟一个参数，大于一个或者没有，退出程序

touch $1                   #以命令后的参数名为文件名，创建文件

if [ -f $1 ]
then
  echo "\"$1\" is a regular file"
fi                          #检测文件格式是否为 普通文件 ，若是，执行then后的语句


echo -n "The file can : "   #输出“The file can : +后面语句的结果” -n表示不换行
if [ -r $1 ]                #检测文件是否可读，
then
  echo -n "r"               #打印r
else
  echo -n "-"               #打印-
fi

if [ -w $1 ]
then
  echo -n "w"
else
  echo -n "-"
fi

if [ -x $1 ]
then
  echo -n "x"
else
  echo -n "-"
fi

echo ""                       #换行

:<<!
检测命令后参数为文件名的文件是否存在，若不存在。则创建该文件，检测并输出该文件的读取权限
输入：
bash lisnxi2.sh file
输出结果：
"file" is a regular file
The file can : rw-



!
