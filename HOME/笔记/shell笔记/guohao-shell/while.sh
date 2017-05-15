#!/bin/bash
# 1到 100  求和

sum=0
i=1
while [[ $i -le 100 ]]; do
  let "sum+=i"
  ((i++))
done
echo "sum= $sum"
