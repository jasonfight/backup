#!/bin/bash
:<<!
for n in {1..1000}
do
  sum=0
  let "num=$n / 2"
  for((i=1;i <= num;i++))
  do
    let "k=$n % $i"
    if [ $k -eq 0 ]
    then
      let "sum+=i"
    fi
  done
  if [ $n -eq $sum ]
  then
    echo -n "$n "
  fi
done
echo ""
!
#:<<!

for (( i = 1; i <= 1000; i++ )); do
  sum=0
  let "num1= $i / 2"                  #求$i所有因子的累加
  for (( a = 1; a <= num1; a++ )); do
      let "num2=$i % $a "
      if [[ num2 -eq 0 ]]; then
          let "sum+=$a"
      fi

  done
      if [[ $sum -eq $i ]]; then
      echo $sum
      fi
done





#!
