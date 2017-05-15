#coding=utf-8
#实际中,views.py不会创建在booksite中,而是在应用中
from datetime import *
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,render_to_response
class A(object):
    a = 1
    def fun(self):
        return "hahahahahahahaha"



def hello(request):
    return HttpResponse('Hello world')

def nihao(request):
    return HttpResponse('你好!!')

def time(request):
    time = datetime.now()
    # now = '''<html><body> nowit's %s </body></html>'''%time

    # NOTE: 这一步之前,需要引入django.template 中的 loader,新建一个templates的文件夹,然后在settings中将该文件夹添加到TEMPLATES中的DIRS中
    # NOTE: 在template中新建一个current_time.html的文件,将模板写入
    t = loader.get_template('current_time.html')

    # NOTE: 在这一步之前,需要引入django.shortcuts中的render
    # NOTE: 将time传递给current_time.html中的current_time,然后整体返回给html
    html = t.render({'current_time':time})
    return HttpResponse(html)

# NOTE: 变量,标签,过滤器的使用
def template_test(request):
    l=['hello','world']
    d={'a':1,'b':2,'c':3}
    c = A()
    message = 'hello world'

#1    # t = loader.get_template('template1.html')
    # html = t.render({'list':l,'dict':d,'class':c,'value':1,'message':message})
    # return HttpResponse(html)

#2    # return render_to_response('template1.html',{'list':l,'dict':d,'class':c,'value':1,'message':message})
#3    # return render_to_response('template1.html',locals())
#4    # return render(request,'template1.html',locals())
    return render(request,'template1.html',{'list':l,'dict':d,'class':c,'value':1,'message':message})
def hours_ahead(request,offset,m):
    print "++++++",m
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.now()+timedelta(hours = offset)
    html = '<html> <body> in %s , it will be %s </body> </html>'%(offset,dt)
    return HttpResponse(html)
