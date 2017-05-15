#!/bin/bash


#输入 1 + 2  打印出结果， 任意数  任意运算符号  计算出结果


yunsuan ()
{
  result=0
if [[ $2 = + ]]; then
  let "result= $1 + $3"
  echo "$1 $2 $3 =  $result"
fi

if [[ $2 = - ]]; then
  let "result= $1 - $3"
  echo "$1 $2 $3 =  $result"
fi

if [[ $2 = * ]]; then

  let "result = $1 * `$3`"
  echo "$1 * $3 =  $result"
fi

if [[ $2 = / ]]; then
  let "result= $1 / $3"
  echo "$1 $2 $3 =  $result"
fi

}
yunsuan $1 $2 $3
echo $1 $2 $3 
