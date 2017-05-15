#!/bin/bash

echo "Input a b c :"
read a b c

echo "before:a = $a,b = $b,c = $c"

if [ $a -ge $b ]
then
  tmp=$a
  a=$b
  b=$tmp
fi                        # 比较a和b的大小 若a大于等于b，将a b 的值调换
if [ $a -ge $c ]
then
  tmp=$a
  a=$c
  c=$tmp
fi                        # 比较a和c的大小 若a大于等于c  将a c的值调换
if [ $b -ge $c ]
then
  tmp=$b
  b=$c
  c=$tmp
fi                          # 比较a和c的大小 若a大于等于c  将a c的值调换

echo "after:a = $a,b = $b,c = $c"


:<<!
从终端中输入a b c 三个数，将其按照从大到小的顺序排列出来。

前两个if  保证 A 的值成为最小

最后一个 if  保证 B 比 C 小

举例：
Input a b c :
8 7 9
before:a = 8,b = 7,c = 9
after:a = 7,b = 8,c = 9





!
