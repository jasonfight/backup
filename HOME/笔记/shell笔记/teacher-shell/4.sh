#!/bin/bash

reverse(){
  n=$1
  rev=0
  sd=0
  while [[ $n -gt 0 ]]; do
    #statements
    sd=`expr $n % 10`
    rev=`expr $rev \* 10 + $sd`
    n=`expr $n / 10`
  done
  echo $rev
}


if [[ $# -ne 1 ]]; then
  #statements
  echo "Usage :$0 number"
  echo "     I will find reverse of given number"
  echo "     For eg.\$1234,I will print 4321    "
  exit 1
fi

echo `reverse $1`
