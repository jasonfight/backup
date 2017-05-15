#!/usr/bin/python
#coding=utf-8
import cgi

reshtml = ''' Content-Type : text/html\n
<html><head><title>
表单
</title></head>
<body>
<h3>friend list for : <i>%s</i> </h3>
姓名:<b>%s</b> <br>
你有 <b>%s</b>个朋友
</body>
</html>'''
from = cgi.FieldStorage()
who = form['text'].value
howmany = from['friendnum'].value
jprint reshtml$(who,who,howmany)
