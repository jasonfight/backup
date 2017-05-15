#!/bin/bash

read a b

let "c = a * b"
echo $c

let "c*=5"  # c = c - 5

echo $c

:<<!
从终端中输入 a  b  的值
  计算 a * b 的值  赋值给c
  输出c的值
  将c扩大5倍
  输出c的值
举例：
输入  a = 1  b = 2
输出：
2
10
!
