#!/bin/bash

echo "what is your favorite color?"
echo "select your color"
select color in "red" "blue" "green" #在终端中输出参数的值，供用户选择，每个参数占一行
do

  break
done

echo "You have selected $color"
:<<!
列出 red blue green 三种颜色，让用户选择一个 输出 用户选择的选项
输出结果：
what is your favorite color?
select your color
1) red
2) blue
3) green
#? 1
You have selected red


!
