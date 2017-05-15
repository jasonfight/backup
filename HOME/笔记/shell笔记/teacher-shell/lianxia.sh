#!/bin/bash
:<<!
sum()
{
  i=1
  sum=0
  while [ $i -le $1 ]
  do
    let "sum+=$i"
    ((i++))
  done
  echo $sum
}

read value
sum $value

从终端输入一个整数n，调用一个累加方程，计算1到n的所有数的和
!
read a

for (( i = 1; i <=a ; i++ )); do
    let "sum+=i**2"

done
  let "sum2=a*(a+1)*(2 * a + 1 ) / 6"
echo $sum
echo $sum2
#求输入数的平方和
