#!/bin/bash

if [ $# -ne 1 ]
then
  echo "Please input arg"
  exit 1
fi

let "n=$1 / 2"

i=1       #i 为计数器
#for i in {1..$n}
while [ $i -le $n ]
do
    let "num=$1 % $i"
    if [ $num -eq 0 ]
    then
      echo -n "$i  "
    fi
    ((i++))
done
echo ""

:<<!
找出一个数的所有因子
思路：
先求出该数值的一半，
从1到该数值的一半分别对该数求余，
如果余数等于0，则计数器加一
最终输出计数器的值，
计数器的值就是该数的因子个数。





!
