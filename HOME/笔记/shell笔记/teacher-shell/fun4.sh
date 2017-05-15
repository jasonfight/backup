#!/bin/bash

#递归调用

fact()
{
    local num=$1
      if [ $num -eq 0 ]
      then
        factorial=1
      else
      let "decnum=num-1"
        fact $decnum
      let "factorial=$num * $?"
      fi
    return $factorial
}
set -x
fact $1

echo "Factorial of $1 is $?"
exit 0
