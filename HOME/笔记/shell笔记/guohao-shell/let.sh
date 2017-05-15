#!bin/bash


read a b
let "c = a+ b"
echo "c="$c
let "c+=5"
echo  "c加等5="$c
let "c-=5"
echo "c减等5="$c
let "c*=5"
echo "c乘等5="$c
let "c/=5"
echo "c除等5="$c
let "c=c**2"
echo "c的平方=$c"
