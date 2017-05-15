#!bin/bash
i=10
while [[ $i -gt 0 ]]; do
  if [[ $i -ge 5 ]]; then
    i=`expr $i - 1`
    continue
  fi
  echo $i
  i=`expr $i - 1`
done
