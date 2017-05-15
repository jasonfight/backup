#!/usr/bin/python
 
import urllib
import re
 
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
 
def getImg(html):
    reg = r'src="(http://.+?\.jpg)"'
     
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    print(imglist)
 
    x = 0
 
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg'%x)
        x+=1
 
html = getHtml('http://tieba.baidu.com/p/4229162765')
 
print (getImg(html))
