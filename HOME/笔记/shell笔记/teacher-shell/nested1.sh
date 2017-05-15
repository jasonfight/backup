#!/bin/bash


for i in {1..8}
do
  for j in {1..8}
  do
    total=$(($i + $j)) #let "total = i + j"
    tmp=$(($total % 2))
    if [ $tmp -eq 0 ]
    then
      echo -e -n "\033[47m  "
    else
      echo -e -n "\033[40m  "
    fi
  done
  echo ""
done
