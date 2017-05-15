#!/bin/bash

array=(1 2 3 4 52 6 7 8)   #数组的定义
echo $array       #打印第一个数
echo ${array[6]}  #打印第七个数
echo ${array[@]}  #打印全部
echo ${array[*]}
echo ${array[2*3]}  #打印第2个数
echo ${array[*]:2:2}
echo "_____________________________"

for i in "${array[@]}"
do
  echo $i
done
echo "-------------------------"
echo "length = ${#array[@]}"
echo "length_${array[4]} = ${#array[4]}"
