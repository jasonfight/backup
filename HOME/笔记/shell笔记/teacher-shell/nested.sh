#!/bin/bash


for i in {1..9}
do
  for ((j=1;j<=i;j++))
  do
#    echo "$i * $j = x"
    let "temp = i * j"
    echo -n "$j * $i = $temp  "
  done
  echo ""
done
:<<!
输出99乘法表

思路：
使用两层循环，第一层循环控制第一个因数为1-9 第二层循环控制
第二个因数及每一行输出的内容。
第一行输出1*1=1
第二行输出 1*2=2  2*2=4

!
