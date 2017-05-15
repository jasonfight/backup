#!/bin/bash

for value          # 将命令后的参数 赋值给 value
do
  echo "value = $value"    #打印value的值
done


:<<!
从命令后的参数读取值并赋值给 value，有几个参数，执行几次for语句




输出结果：

输入：bash for2.sh 1 2 3
输出：
value = 1
value = 2
value = 3

!
