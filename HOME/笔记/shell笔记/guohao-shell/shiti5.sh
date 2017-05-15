#!/bin/bash

#打印一个给定数字的反序,将此功能写成一个函数
:<<!
思路：
1.将输入的数字num ，用10对其求余 ，余数就是个位上的数字
2.将输入的数字除以10，十位上的数字位移到个位上，重复第一步骤
3.用一个计数器保存该数字的位数，循环一次，技术器加一
4.用第一次求得的数乘以10 的 计数器的值的次方，加到最后一位。
!
:<<!
if [[ $# -ne 1 ]]; then
  echo "please input a num!"
  exit 1
fi
!
num=$1
i=1
array=()
while [[ $num -ne 0 ]]; do
  let "a = num % 10 "
  let "M$i= num %10"
  echo "M$i=$M$a"

  let "num = num / 10"
  ((i++))
done

echo "M1="$M1
echo "----------------"
for (( j = 1; j <i ; j++ )); do
  echo "M1="$M1
  echo "M$j=${M$j}"
  echo "---------------"
done





:<<!

    j=0
  while [[ $i -gt 0 ]]; do
    #echo ${array[$j]}
    let "b = ${array[$j]} * 10** `expr $i - 1`"
    #echo "b=$b"
    let "result+=$b"
    ((j++))
    ((i--))
  done
  echo "result = $result"
}
!
