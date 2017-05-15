#!/bin/bash


a=1
b=1

for (( b = 1; b <= 9; b++ )); do
  for (( a = 1; a <= b; a++ )); do
    let "result=a*b"     #(())
    echo  -n "$a*$b=$result "
  done
  echo ""
done


:<<!
while [[ $b -le 9 ]]; do
  a=1
  while [[ $a -le $b ]]; do
    let "result=a*b"     #(())
    echo  -n "$a*$b=$result "
((a++))
  done
  ((b++))
    echo ""
done
!
