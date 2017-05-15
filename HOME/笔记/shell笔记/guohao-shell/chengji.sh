#!/bin bash

read chengji
 if  [ $chengji -gt 100 -o $chengji -lt 0 ]
 then
 echo "成绩输入错误"
 exit 1
 elif [[ $chengji -ge 90 ]]
 then
   echo "成绩为a"
 elif [[ $chengji  -ge 80 ]]
 then
   echo "成绩为b"
 elif [[ $chengji -ge 70 ]];
 then
    echo "成绩为c"
  elif [[ $chengji -ge 60 ]];
  then
    echo "成绩为d"
  else
    echo "成绩不及格"
fi
