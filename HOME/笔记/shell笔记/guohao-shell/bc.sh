#!/bin/bash


read a b
value=`echo "$a + $b"|bc`
echo $value
