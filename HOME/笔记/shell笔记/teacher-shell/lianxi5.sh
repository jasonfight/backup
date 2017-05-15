#!/bin/bash

echo -n "Input a year:"
read year

let "n1 = $year % 4"
let "n2 = $year % 100"
let "n3 = $year % 400"
echo $n1
echo $n2
if [ $n1 -eq 0 -a $n2 -ne 0 ] || [ $n3 -eq 0 ]
then
  echo "$year 是闰年"
else
  echo "$year 不是闰年"
fi


:<<!
从终端中输入一个年份 判断是否是闰年
思路：
1 年份能被4整除且不能被100 整除  是闰年
2 年份能被400 整除 是闰年


!
