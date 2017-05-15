#!/usr/bin/python
#coding=utf-8
'''
14. 创建一个数据库，使用python操作如下：
    1.创建表包含id、name、age、score四个字段，其中id为主键，所有字段均不能为空，score默认值为0
    2.在表中插入3条数据
    3.通过查找打印出所有分数小于60的人的信息
'''

import MySQLdb

db = MySQLdb.connect('localhost','root','123','mmm')
cursor = db.cursor()
cursor.execute("drop table if exists test")
sql='create table test (id tinyint not null primary key,\
name varchar(20) not null,age tinyint not null,score int not null default 0)'
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
sql='insert into test values (1,"guohao",23,40)'
cursor.execute(sql)
db.commit()
sql='insert into test values (2,"gasol",23,40)'
cursor.execute(sql)
db.commit()
sql='insert into test values (3,"fisher",23,80)'
cursor.execute(sql)
db.commit()
sql='select * from test where score < 60'
cursor.execute(sql)
data = cursor.fetchall()
for i in data:
    for a in range(3):
        print i[a],
    print ''
