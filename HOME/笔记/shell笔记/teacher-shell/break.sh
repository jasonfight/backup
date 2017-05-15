#!/bin/bash

i=10
while true
do
  echo $i           # 输出10
  i=`expr $i - 1`   # i递减
  if [ $i -le 5 ]   # 判断 i是否小于5
  then
    break           # 跳出循环
  fi
done
:<<!

i取10 依次输出递减1后的数值，当i小于等于5时，结束循环。\
输出结果：
10
9
8
7
6

!
