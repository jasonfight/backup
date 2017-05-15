#!/bin/bash

read a b

value=`echo "$a + $b" | bc`

echo $value


!<<!
从终端中输入 a b 的值
将 a + b（均为小数） 的值  赋值给 value
输出value的值

eg：
输入
1.1 2.2
输出：
3.3

!
