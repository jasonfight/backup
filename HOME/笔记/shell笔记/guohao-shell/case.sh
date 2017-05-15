#!/bin/bash



read value

case $value in
  20|30)
  echo "value = 20";;
  30)
  echo "value = 30"
  ;;
  40)
  echo "value = 40"
  ;;
  *)
  echo "others"
esac


read value2
case $value2 in
  10)
  echo "value = 10"
  ;;
 50)
 echo "value - 50"
 ;;
 *)
 echo "others"
esac
