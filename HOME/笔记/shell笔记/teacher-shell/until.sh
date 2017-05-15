#!/bin/bash

i=0

until [[ $i -gt 5 ]]
do
  let "square=i*i"
  echo "$i * $i = $square"
  let "i++"
done
:<<!
计算0到5的平方
输出结果：
0 * 0 = 0
1 * 1 = 1
2 * 2 = 4
3 * 3 = 9
4 * 4 = 16
5 * 5 = 25


!
