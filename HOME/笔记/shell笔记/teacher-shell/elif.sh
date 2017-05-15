#!/bin/bash

if [ $# -ne 1 ]
then
  exit 1
fi          #判断参数个数是否为1，不唯一 则退出脚本


if ! [ -e $1 ]
then
  echo "The $1 not exist!"
  exit 1      #检测以参数内容为文件名的文件是否存在，如果不存在 退出
fi

if [ -f $1 ]
then
  echo "$1 是一个文件"
elif [ -d $1 ]
then
  echo "$1 是一个目录"
else
  echo "$1 是其他文件类型"
fi

:<<!
检测一个输入的文件名 是否存在，并检测输出该文件的文件类型，输出该文件为文件类型，目录或者其他类型
