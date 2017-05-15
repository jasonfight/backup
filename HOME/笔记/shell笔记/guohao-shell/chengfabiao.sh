#!/bin/bash

#打印第二行
a=1
b=1
i=9

if [[ $i -eq 9 ]]; then
  while [[ $b -le 9 ]]; do
    let "result=a*b"
    echo -n "$a*$b=$result" ' '
    ((b++))
    ((a++))
  done

fi
