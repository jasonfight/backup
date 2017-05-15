#!/bin/bash
set -x

read value

ji=0
ou=0

for i in $value
do
  let "num=$i % 2"
  if [ $num -eq 0 ]
  then
    let "ou+=$i"
  else
    let "ji+=$i"
  fi
done

echo "ji = $ji"
echo "ou = $ou"
:<<!
从终端中输入一系列数字，计算出所有奇数的和和偶数的和
思路：
1.用2依次对输入的数进行求余，看余数是否为0
2.如果余数为0，则累加到偶数中，如果不为0，则累加到奇数中，
3.输出最后的奇数的累加结果和偶数的累加结果

举例：

输入 1 2 3 4 5 6 7 8
输出： ji=16
      ou=20

!
