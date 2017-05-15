#!/bin/bash

echo -n "Input a num >"

read num
n=0

while true
do
  let "k = num % 10"
  if [ $k -eq 1 ]
  then
    let "n+=1"
  fi

  let "num = num / 10"
  if [ $num -eq 0 ]
  then
    break
  fi
done

echo "n = $n"

:<<!
思路：
1.将输入的数用10 进行求余，余数即为个位上的数，
2.判断个位上的数是否等于1，如果等于1，则计数器加1
3.用10 对输入的数进行整除，得到的数就是原先的数去掉个位的数，再重复第1、2步骤，
直到最后一位数除以10后的结果是0时，结束循环。 输出记数器的值

echo "please input a number:"
read num
n=0
while true
do
  let "a=$num % 10 "
if [[ $a -eq 1 ]]; then
      ((n++))
fi

  let "num= $num / 10"
  if [[ $num -eq 0 ]]; then
      break
  fi
done

echo $n



!
