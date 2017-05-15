#!/bin/bash

array=(5 4 3 6 1 2 8 7 9 )
set -x
let "length=${#array[@]}-2"
for i in ${array[@]}
do
    n=1                    #第一个数与后面所有的数比较
  until [[ $n -eq $length ]]; do
      if [ $i -ge ${array[i+n]} ]
      then
        tmp=$i
        $i=${array[i+1]}
        ${array[i+1]}=$tmp
        ((n++))
      fi
  done
  done
  echo ${array[@]}
