#/bin/bash

:<<!
1. 使用shell脚本中的循环编程完成，求从1到10的和。要求用while循环和for循环两种方法。
!
for (( i = 1; i <= 10; i++ )); do
    let "result += i"
done
echo $result


while [[ $i -le 10 ]]; do
    let "result += i"
done
echo $result
