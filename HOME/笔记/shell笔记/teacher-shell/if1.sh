#!/bin/bash

#if 的嵌套
read value

if [ $value -gt 10 ]
then
  echo "value > 10"

else
#  echo "value <= 10"
  if [ $value -lt 6 ]
  then
    echo "value < 6"
  else
    echo "10 >= value >= 6"

  fi
fi

:<<!

从终端读取一个数
 如果大于10  输出 value >10
 如果小于6  输出 value < 6
如果 大于等于6 小于等于10  则输出 value<=10

!
