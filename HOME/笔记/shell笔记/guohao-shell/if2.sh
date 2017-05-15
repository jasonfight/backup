#!bin/bash

read value
if [[ $value -gt 10 ]]
then
     echo "value > 10"
else
     echo "value <= 10"
fi
 #从终端输入三个数，将3个数按照从小到大顺序打印出来
 read a b
if [[ $a -gt $b ]]; then
  a ^= b
  b ^= a
  a ^= b
  echo $a $b
fi
