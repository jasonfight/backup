#!/bin/bash

array=(1 2 3 4 "hello" 6 7 8) #数组的定义


echo $array                 # 输出第一个数
echo ${array[5]}             #输出第六个数
echo ${array[@]}             #输出所有数
echo "++++++++++++++++++++++++++++++++"
for i in "${array[@]}" # *->"1 2 3 4 5 6 7 8"
do                          # @-> "1" "2" "3" ......
  echo $i
done
echo "++++++++++++++++++++++++++++++++"

echo "length = ${#array[@]}"        #输出数组的长度
echo "length_n = ${#array[n]}"        #输出 数组中 第N+1 个数的 长度

:<<!

echo ${#array[4]}  #输出数组中第5个数的长度





!
