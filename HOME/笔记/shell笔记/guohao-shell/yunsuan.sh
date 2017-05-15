#!bin/bash



#rsult1=`expr 2 \* 3 + 15 - 18 / 3`
let "result = 2 * 3 + 15 - 18 / 3"
echo "result1 = $result"


a=2
b=3
c=15
d=18


result2=`expr $a \* $b + $c - $d / $b`
echo "result2=$result2"
