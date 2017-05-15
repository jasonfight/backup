#!/bin/bash

#创建一个文件 名为file，然后测试文件是否创建成功，并打印文件的读写执行权限
touch file

if [ $# -eq 1 ]
then
  exit 1
fi
read $1
if [ -f $1 ]
then
  echo "\"$1\"""is a regular file"
fi


echo -n "The file can : "
if [ -r $1 ]
then
  echo -n "r"
else
  echo -n "-"
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

echo ""
