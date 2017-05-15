#!/bin/bash

a=10
b=2

sum=`expr $a + $b`
min=`expr $a - $b`
mul=`expr $a \* $b`
div=`expr $a / $b`
yu=`expr $a % $b`
mi=`expr $a ** $b`

echo "sum = $sum"
echo "min = $min"
echo "mul = $mul"
echo "div = $div"
echo "remain = $remain"
echo "pow = $pow"


:<<!
加   sum           sum
减 - min           minus
乘 \* mul          multiply
除 /  div          division
求余 % remain      remainder
幂函数 **  pow      power





!
