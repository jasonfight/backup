#!/bin/bash

read a b
temp=0
if [[ $a -gt $b ]]
then
temp=$a
a=$b
b=$temp
   echo $a $b
fi
