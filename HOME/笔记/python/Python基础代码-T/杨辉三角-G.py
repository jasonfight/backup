#!/usr/bin/python
#coding=utf-8
'''
功能要求: 输出杨辉三角.
思路: 1.先声明一个阶梯式列表,一共两层,第一层 为1,第二层为1,1
     2. 使用两层循环,第一层循环控制层数,从第三层开始循环,循环n层每一次循环开始时,用[1,1]为该层初始数据
     3. 第二层循环控制最底层添加的数,循环次数为 n-1次 及底层比上一层增加 n-2 个数,每一次从第二位置开始,到第n-1位结束
     4. 循环完毕后,生成总的阶梯式列表,
     5, 使用两层循环,从各层列表中取数,第一层循环控制层数,第二层循环负责遍历该层列表的所有数.然后输出

'''
#自己代码:
l=[[1],[1,1]]
n=4

for i in range(2,n):
    l.append([1,1])
    for j in range(1,i):
        l[i].insert(j,l[i-1][j-1]+l[i-1][j])
print "l=",l

for x in range(n):
    for y in range(x+1):
        print l[x][y],
    print ""
'''
老师代码:
a = input()
l = [ [1],[1,1] ]
for i in range(2,a):
    l.append([1,1])
    for j in range(1,i):
        l[i].insert(j,(l[i-1][j-1]+l[i-1][j]))
for x in range(len(l)):
    for y in range(x+1):
        print l[x][y],
    print ''
'''
