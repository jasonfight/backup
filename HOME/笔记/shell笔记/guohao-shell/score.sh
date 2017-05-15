#!/bin/bash



read score
score=`expr $score / 10`
case $score in
  9|10)
  echo "a"
  ;;
  8)
  echo "b"
  ;;
  40)
  echo "value = 40"
  ;;
  *)
  echo "others"
esac
