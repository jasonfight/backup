#!/bin/bash

read a b c d                  #从终端中读取 a b c d 的值

result=`expr $a \* \( $b + $c \) - $d / $b`     #计算 a*(b+c) - d/b

echo "result = $result"                         #输出result的值



:<<!
从终端中读取 a b c d 的值
计算a*(b+c) - d/b的结果。


取  a=1 b=2 c=3 d=4
及 1*(2+3)-(4/2)=5-2=3
输出结果：
1 2 3 4
result = 3




!
