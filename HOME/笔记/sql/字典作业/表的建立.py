#!/bin/python

import MySQLdb

db = MySQLdb.connect('localhost','root','123','dict')
cursor = db.cursor()
sql = 'create table usr (id tinyint NOT NULL AUTO_INCREMENT PRIMARY KEY)'
try:
    cursor.execute(sql)
except:
    db.rollback()

sql = 'alter table usr add column (name varchar(20) NOT NULL )'
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

sql = 'alter table usr add column (password varchar(10) NOT NULL )'
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

sql = 'create table history (id tinyint NOT NULL AUTO_INCREMENT PRIMARY KEY)'
try:
    cursor.execute(sql)
except:
    db.rollback()

sql = 'alter table history add column (name varchar(10) NOT NULL )'
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

sql = 'alter table history add column (history text NOT NULL )'
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

sql = 'alter table history add column (time varchar(50) NOT NULL )'
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
