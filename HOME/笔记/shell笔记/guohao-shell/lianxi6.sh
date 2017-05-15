#!/bin/bash
#从终端输入文件名  在当前文件夹中查找，存在 输出该文件存在，不不存在 输出 不存在，不允许用-e


for file in $filelist
do
  if [[ $1 = $file ]]; then
    echo "$1 is exist"
    exit 0
  fi
done
echo "$1 is not exist"
