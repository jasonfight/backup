#!/bin/bash

sum()
{
  sum=`expr $1 + $2`      #函数内的 $1 $2 从 调用函数时传参
  echo $sum
}

sum 1 2

echo $1              # 从执行脚本时传参


:<<!

局部变量 和全局变量 的区别


函数内的 $n  从调用函数时传参

函数外的 $n  从执行脚本是传参

距离：

执行 bash fun1.sh “nihao”
输出结果：
3
nihao







!
