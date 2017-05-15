#!/bin/bash

str=`find ./ -name \*.html`
for i in $str
do
	echo "$i"
	mv $i ${i/html/-t.html}
done
