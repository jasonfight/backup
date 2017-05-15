#! /bin/bash


read nianfen

if [[ $nianfen % 4 ]];
then
  echo "$nianfen 年是闰年"
fi
