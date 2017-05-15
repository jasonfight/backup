#!/bin/bash

count()
{
  if [ $# -ne 3 ]
  then
    echo "The number of argument is not 3"
  fi

  s=0

  case $2 in
    +)
    let "s = $1 + $3"
    echo "$1 + $3 = $s"
    ;;
    -)
    let "s = $1 - $3"
    echo "$1 - $3 = $s"
    ;;
    \*)
    let "s = $1 * $3"
    echo "$1 * $3 = $s"
    ;;
    \/)
    let "s = $1 / $3"
    echo "$1 / $3 = $s"
    ;;
    *)
    echo "What you input is wrong!"
  esac
}

echo "Please type your word (e.g. 1 + 1) "
read a b c
count $a $b $c




:<<!
算数计算  输入 1 + 1  计算出结果并输出（目前不能使用乘法运算） 



!
