#/bin/bash
:<<!
1. 使用shell编程完成。从终端或命令行输入一系列是数列，
筛选其中的偶数在终端打印出来
思路:
1.使用一个循环,从1开始,一直到传参数的个数为止,每循环一次,将传入的参数掺入循环执行一遍
2.将传入的参数进行判断,如果用2对其求余,结果为0,则进行输出.

!



for (( i = 1; i <= $#; i++ )); do
    let "s = $i % 2 "
    if [[ s -eq 0 ]]; then
    echo $i
    fi
done
