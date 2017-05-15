#!/bin/bash


ai()
{
  let "sum=$1 + $2"
  echo $sum
  echo "你好"
}
ai 1 2
value=`sum=$1 -$2`
echo $value
