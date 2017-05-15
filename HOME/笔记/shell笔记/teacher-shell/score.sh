#!/bin/bash

echo -n "Please input a score >"
read score

if [ $score -lt 0 -o $score -gt 100 ]
then
  echo "Input error !!!"
  exit 1
fi                                #判断从终端中输入的值是否合法（大于0且小于100）

num=`expr $score / 10`            #将分数除以 10  得到数值为 1-10 中的一个

case $num in                       #如果等于 9或者10，执行下一个分号前的命令
  9 | 10)
  echo "A"
  ;;
  8)                                #如果等于8 ，执行下一个分号前的了命令
  echo "B"
  ;;
  6 | 7)
  echo "C"
  ;;
  *)
  echo "not pass..."
esac

:<<!
从终端中输入分数，该分数在[0 100] 区间，判断其成绩等级，

输入： 80
输出：
Please input a score >80
B






!
