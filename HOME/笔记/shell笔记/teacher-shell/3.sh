#!/bin/bash

fileinfo=($(du ./*))
length=${#fileinfo[@]}

for ((i=0;i < $length;i=$((i+2))))
do
  if [[ ${fileinfo[$i]} -ge 10 ]]; then
    #statements
    mv ${fileinfo[$((i+1))]} /tmp
  fi
done
