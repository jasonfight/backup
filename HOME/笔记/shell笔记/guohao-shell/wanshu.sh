

#一个是恰好等于其因子之和，称为完数，找出1000以内所有的完数

#1.先求出所有的因子，
#2 求出所有因子的累加之和 sum
#3 比较 sum 和 原来的数是否一样


for (( n = 1; n <= 1000; n++ )); do
        let "num= $n / 2"
    sum=0
    for (( i = 1; i <= num; i++ )); do
      let "yu= $n % $i "
      if [[ $yu -eq 0 ]]; then
        let "sum+=i"
      fi
      done
      if [[ $sum -eq $n ]]; then
        echo "$n 是完数"
      fi
done
