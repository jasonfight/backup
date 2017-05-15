#!bin/bash

#while 的类C用法
# 求加和运算
i=1
sum=0
while((i<=100))
do
  let "sum=$sum + $i"
  ((i++))
done
echo $sum
