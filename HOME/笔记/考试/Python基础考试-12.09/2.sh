#/bin/bash
:<<!
2. 使用shell完成生成六位随机的验证码，
验证码包含0-9的数字和任意a-z的字母。

提示：使用$RANDOM系统函数的到一个随机数，
通过取余限定随机数范围可完成要求。可通过man手册查询帮助


要生成 a-b 的随机数  c=b-a+1   random 后跟的格式为 c+a
思路:
1.先用一个循环,循环六次,每一次循环产生一个0-9的随机数
2.使用一个循环,将26个字母生成一个数组
3.通过随机产生一个索引值,来产生一个随机字母
4,将随机数字与随机字母输出即可
!

for (( i = 0; i < 6; i++ )); do
    echo -n $(($RANDOM%10))
done

i=0
for i in {a..z};do
  b[$j]=$i
  let j++
done
((n=RANDOM%26))
echo ${b[$n]}
