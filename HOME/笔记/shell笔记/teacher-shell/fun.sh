#!/bin/bash

fun() {
  echo "hello world!"
}

fun
let "sun=1+2"
echo "This is a function : `fun` $sun  "
echo "  `expr 1 + 2 `  "


:<<!

    函数名（）
    {
      函数内容
    }             #声明函数，声明函数必须在调用函数之前
函数名   #调用函数





!
