#!/bin/bash
if [[ $# -ne 1 ]]; then
  echo "命令后面需要输入待检测的文件名"
  exit 1
fi
if ! [ -e $1 ]; then
   echo "文件不存在"
   exit 1
fi
if [[ -f $1 ]]; then
  echo "$1是一个文件"
fi
if [[ -d $1 ]]; then
  echo "$1是个文件夹"
  fi
else
echo "$1是其他类型文件"
