#!/bin/bash

#显示当前目录中，存在多少个文件和目录
f=1
d=1


for i in  `ls`
do
    if [[ -f $i ]]; then
      let "n+=1"
    fi
    if [[ -d $i ]]; then
      let "m+=1"
    fi
  echo "$i"
done
echo $n
echo $m
