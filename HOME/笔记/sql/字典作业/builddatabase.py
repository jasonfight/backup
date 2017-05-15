#!/usr/bin/python
#coding=utf-8

import MySQLdb

db = MySQLdb.connect('localhost','root','123','dict')
cursor = db.cursor()
