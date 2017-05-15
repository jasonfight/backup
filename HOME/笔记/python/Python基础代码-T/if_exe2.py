# !/usr/bin/python

#输入一个学生成绩，判断学生等级

score = float(input("input the score:"))

if score < 0 or score > 100:
    print("sorry your input error")
else:

    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('Sorry you lost')
