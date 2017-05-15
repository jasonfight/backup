#!/bin/bash

if [ $# -ne 1 ]
then
  exit 1
fi

filelist=`ls`

for file in $filelist
do
  if [ $1 = $file ]
  then
    echo "find $1..."
    exit 0
  fi
done

echo "not find $1...."

:<<!
在当前文件夹下查找一个文件。判断文件是否存在，存在 数出 找到该文件   不存在则输出找不到该文件。




!
