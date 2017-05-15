#!/bin/bash

str=`find ./ -name \*.sh`

for i in $str
echo $i
do
	mv $i ${i/sh/shell}
done
