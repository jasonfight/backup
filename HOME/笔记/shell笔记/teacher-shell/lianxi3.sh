#!/bin/bash

read value                #从终端读取value的值

if [ $value -gt 50 ]      #如果value大于50，执行then语句
then
  if [ $value -gt 100 ]   #如果value大于100 执行下一个then语句
  then
    echo "value > 100"
  else                     #value小于等于100
    if [ $value -gt 80 ]   #如果 value 大于80 且 小于等于 100，执行下一个then语句
    then
      echo "80 < value <= 100"
    else                    # value 小于等于 80 且 大于50
      echo "50 < value <= 80"
    fi
  fi
else                      #value 小于等于 50
  if [ $value -ge 0 ]       #如果 value 大于等于0 且小于等于50
  then
    echo "0 <= value <=50"
  else                  # value 小于 0
    echo "value < 0"
  fi
fi
:<<!
从终端中输入一个数值，判断数值 在 （100 +～） (80 100]  (50 80] [0 50] ( -~ 0)
中的哪一个区间

!
