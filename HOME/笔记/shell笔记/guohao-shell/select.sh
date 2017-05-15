#!/bin/bash


echo "what is your favorite color?"
select color in "red" "blue" "green" 1 2 
do
  echo "select your  color"
  break
done
echo "your favorite color is $color"
