#!/bin/bash

# 从终端输入一个数，列出这个数的所有因子。
  if  [ $# -ne 1 ]
  then
   echo "请输入被除数"
  exit 1
fi

n=`expr $1 / 2`       #$1为终端中输入的第一个数，  先取其一半

while [[ $i -le $n ]]; do
  let "num=$1 % $n"
  if [[ $num -eq 0 ]]; then
    echo "$i"
  fi
  ((i++))
done
