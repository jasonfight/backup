#!/bin/bash

directory()
{
filenum=0
dirnum=0

ls
echo ""

for file in `ls`
do
  if [ -d $file ]
  then
    let "dirnum += 1"
  elif [ -f $file ]
    let "filenum += 1"
  fi
done

echo "The number of dirctories is $dirnum"
echo "The number of files is $filenum"

}

directory


:<<!
目的：判断当前文件夹中的所有文件的文件类型，输出普通文件数和文件夹数
思路：
1.先将当前文件夹中所有文件列出来，
2.将所有文件逐一赋值给一个变量
3.判断这个变量 是文件还是目录
4.如果是文件 文件计数器加一 如果是目录  目录计数器加一
lianxi5.sh



!
