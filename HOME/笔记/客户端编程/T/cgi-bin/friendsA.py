#!/usr/bin/python

import cgi

reshtml = '''Content-Type : text/html\n

<html><head><title>
Friends CGI Demo (dynamic screen)
</title></head>
<body><H3>Friends list for:<I>%s</I></H3>
your name is :<B> %s </B><P>
you have <b>%s</b> friends.
</body></html>'''

form = cgi.FieldStorage()
who = form['person'].value
howmany = form['howmany'].value

print reshtml%(who,who,howmany)
