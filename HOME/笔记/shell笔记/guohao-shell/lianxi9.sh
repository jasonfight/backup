#!/bin//bash

#输入一个整数，判断这个整数中，有多少个1


#用10对输入的数进行求余，如果为1，计数器加1
#如果不为1 则将数值除以10，得到另一个数 num再进行第一步
#如果num为0，则停止计算，输出计数器的值
echo $@
let "i=$@"
while true
  do
  let "a=i%10"
    if [[ $a -eq 1 ]]; then
      let "n+=1"
    fi
      let "i=i / 10"
      if [[ $i -eq 0 ]]; then
        break
      fi
done
echo $n

:<<！
举例： 输入12
i=12
n=0
a= 12 % 10 = 2  不等与1 不执行第一个if
i = 12 / 10 = 1，不等于0，不执行第二个if
i=1
n=0
a= 1 % 10 = 1 执行第一个if n+=1，n为1
num= 1 / 10 = 0 执行第二个if， 跳出循环，
输出n=1
！
