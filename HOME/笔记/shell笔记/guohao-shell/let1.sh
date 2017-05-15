#！bin/bash

let "a = 4 >> 2"   #4的位数减2

let "b = 4 ^ 6"
let "c = 4 | 6"
let "d = 4 & 6"
let "e = ~4"

echo "a="$a
echo "b="$b
echo "c="$c
echo "d="$d
echo "e="$e

f=4
let "g=(f++)"  #  ++ 在后  先赋值  再自加，++在前  先自加 再赋值
echo "g=$g"
echo "f=$f"

h=4
let "i=(h--)"  #  ++ 在后  先赋值  再自减，++在前  先自减 再赋值
echo "i=$i"
echo "h=$h"
((h--))
echo $h
