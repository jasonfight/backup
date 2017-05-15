#！/bin/bash


#求1到100 的加和

for (( i = 1; i <= 100; i=i+1 )); do   # 声明 i为1   判断 1是否小于等于100 为真，执行第三个语句
  total=`expr $total + $i`
done
echo "the result is $total"


# 计算 1到 10 的加和
for (( j = 1; j <= 10; j++ )); do
  result=`expr $result + $j`
done
echo "the result is $result"
