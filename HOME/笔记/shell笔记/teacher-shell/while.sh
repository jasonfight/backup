#!/bin/bash

sum=0
i=1

while [ $i -le 100 ]
do
  let "sum+=i"
  ((i++))
done


:<<!
计算1到100的累加之和



!
