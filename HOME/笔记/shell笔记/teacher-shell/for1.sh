#!/bin/bash

sum=0

for i in {1..100..2}
do
  let "sum+=$i"
#  echo -n $i
done

echo "sum = $sum"


:<<!
输出100以内的所有奇数的总和
思路：
从i=1开始，以2为单位递增，一直到i=100，每增加一次，将值累加到sum
循环完毕后，sum的值就是100以内所有奇数的总和，输出sum


sum+=$i  将i的值累加到sum






!
