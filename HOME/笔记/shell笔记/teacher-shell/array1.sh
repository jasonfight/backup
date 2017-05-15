#!/bin/bash

array=(1 2 3 4 5 6 7 8) #数组的定义



echo ${array[*]:0}      #1 2 3 4 5 6 7 8
echo ${array[*]:3}     #4 5 6 7 8
echo ${array[*]:2:2}    #3 4

echo ${array[@]}         #1 2 3 4 5 6 7 8
array[3]=10
echo ${array[3]}
array[4]=${array[7]}
echo ${array[@]}           #1 2 3 10 8 6 7 8

i=6

echo ${array[$i + 1]}        #输出 第 6+1+1=7 个数的值


:<<!
${array[@]:0}    数组的所有值，从第一位开始
${array[@]:2}    数组从第三位开始的值
${array[@]:2:2}   数组从第三为位开始读取，读取两位
array[3]=10       将 10 赋值为 array 第4位
array[3]=${array[4]}  将数组第5位 赋值给第4位

${array[$i+1]}    数组 从第$I +2 位开始

!
