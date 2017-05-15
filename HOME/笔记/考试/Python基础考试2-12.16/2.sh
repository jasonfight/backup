#!/bin/bash



if [[ -e dirdir ]]; then
  rm dirdir -rf
fi
mkdir dirdir

b=`ls`
for a in $b
do
  if [ -d $a ]
  then mv $a dirdir
  fi
done

if [[ -e filedir ]]; then
  rm filedir -rf
fi

b=`ls`
mkdir filedir
for a in $file
do
  if [ -f $a ]
  then
    mv $a filedir
  fi
done
tar -czvf filedir.gz filedir
tar -cjvf dirdir.bz2 dirdir
tar -xvf dirdir.bz2
tar -xvf filedir.gz
