#!/bin/bash

i=10
while [ $i -gt 0 ]    #当i大于0时 执行while语句，作用是在i=0的时候，结束
do
  if [ $i -ge 5 ]   # 当i 大于等于5时，执行if语句
  then
    i=`expr $i - 1`   # 将i递减
    continue          #执行下一次循环
  fi
  echo $i             #输出 i
  i=`expr $i - 1`     #将i递减
#done

:<<!
将i=10 进行递减，当i小于5时，输出i的值
输出结果：
4
3
2
1
!
