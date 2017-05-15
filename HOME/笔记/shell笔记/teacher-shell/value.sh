#!/bin/bash

value=1
#unset value
value="1          1"
echo "$value"             #释放value的值
value="hello       world"
echo "$value"

echo hello          kitty
echo "hello          kitty $value"
echo 'hello          kitty $value'
:<<!

输出结果：
hello       world
hello kitty
hello          kitty hello       world
hello          kitty $value





!
