#!/bin/bash


let "a = 4 >> 1"
let "b = 4 ^ 2"
let "c = 4 | 6"
let "d = 4 & 6"
let "e = ~4"

echo   "a = 4 >> 1 ="   $a
echo    "b = 4 ^ 2 ="  $b
echo   "c = 4 | 6 ="   $c
echo   "d = 4 & 6 ="   $d
echo   "e = ~4 ="   $e

f=4

#f++ ==  f = f + 1
#f-- ==  f = f - 1

let "k = f--"
echo "k = $k"         #f--  f在前  先赋值，在-1   --f   --  在前  先-1  在赋值
echo "f = $f"
((f++));
echo $f
