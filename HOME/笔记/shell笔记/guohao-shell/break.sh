#!bin/bash
i=10
while [[ $i -gt 0 ]]; do
    i=`expr $i - 1`
  if [[ $i -le 5 ]]; then
    break
  fi
  echo "$i"
done
