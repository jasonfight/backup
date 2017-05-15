#!/bin/bash
check_user()
{
user=`who | grep -e  "^\<$1\>" | wc -l`   # 开头部分绝对匹配 $1
if [[ $user -eq 0 ]]; then
  return 0
else return 1
fi
}

while true
do
  echo "Input username:/c"
  read uname
  check_user $uname
  if [[ $? -eq 1 ]]; then
  echo "user $uname online"
  else echo "user $uname offline"
  fi
done
