#!/bin/bash

#if 的嵌套

read value

if [[ $value -gt 100 ]]; then
   echo "value >100"
else      #value <=100
   if [[ $value -le 80 ]]; then
     if [[ $value -ge 50 ]]; then
       echo "value=[50 80]"
     else #value<50
       if [[ $value -ge 0 ]]; then
         echo "value[0 50]"
       else
         echo "value=(~ 0)"
       fi
   fi
   fi
fi
