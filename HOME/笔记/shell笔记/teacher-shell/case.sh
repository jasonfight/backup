#!/bin/bash

read value
case $value in
  20 | 30 )
    echo "value = 20 or 30"
    ;;
  "hello")
    echo "value = hello"
    ;;
  40)
    echo "value = 40"
    ;;
  *)
    echo "others"
esac


:<<!
read value
case $value in
1)
  echo "执行第一选项"
;;
2)
echo "执行第二选项"
;;
*)
echo  "没有匹配选项时执行该命令"

esac
!
