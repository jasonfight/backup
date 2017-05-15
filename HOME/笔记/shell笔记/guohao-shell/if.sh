#!bin/bash

value=20
if [[ $value -gt 10 ]]; then
  echo "value > 10"
fi



#创建一个文件 名为file，然后测试文件是否创建成功，并打印文件的读写执行权限

touch file
a=`test -e file`
r=`test -r file`
w=`test -w file`
x=`test -x file`
echo "$a"


if [[ $a  -eq 0 ]]; then
    echo "文件创建成功"
fi
if[ $w -eq 0 ]
then echo "r"
fi
