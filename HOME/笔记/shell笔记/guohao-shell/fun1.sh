#! /bin/bash
#写一个函数  传进去一个数值 求出1到这个数值的加和


result()
{
    if [[ $1 -ge 1 ]]; then
      result=0
  for (( i = 1; i <= $1; i++ )); do
    let "result=result+i"
  done

  echo "1到$1的加和为$result"
    fi
    if [[ $1 -lt 1 ]]; then
      echo "输入错误"
    fi
}
result $1
