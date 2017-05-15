#!/bin/bash

total=0

for((j=1;j<=100;j++));    #j=1，递增到j=100
do
#  total=`expr $total + $j`    #将j的值累加到 total中
  let "total+=j"
done
echo "The result is $total"   #输出累加的值


:<<!
计算1-100的累加之和


输出结果：
The result is 5050

!
