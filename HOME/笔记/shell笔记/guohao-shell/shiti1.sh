#!/bin//bash



#求出100以内的质数

#set -x

for (( i = 2; i < 100; i++ )); do
      let "n=i/2"
    k=0
  for (( j = 1; j <= n  ; j++ )); do
    let "num=i % j"
    #echo "num=$num"
    if [[ $num -eq 0 ]]; then
      let "k+=1"
      #echo "k=$k"
    fi
  done
  if [[ $k -eq 1 ]]; then
    echo "质数为$i"
  fi
done



:<<!

i=1
while [[ $i -le 100 ]]; do
  flog=1
  for (( j = 1; i <= i; i++ )); do
    if [[ $(($i%$j)) -eq 0 ]]; then
      flog =0
      break
    fi
  done
  if [[ $flog -eq 1 ]]; then
    echo $i
  fi
  ((i++))
done

!
