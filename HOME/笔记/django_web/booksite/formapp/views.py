#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from formapp.forms import *
from models import *

# Create your views here.
def search_form(request):
    return render(request,'search_form.html',{})

def search(request):
    if 'usr' in request.GET and request.GET['usr']:
        a = request.GET['usr']
        print '--------------',a # NOTE: 在服务器中打印a,用于测试
        return HttpResponse('Thanks')
    else:
        return render(request,'search_form.html',{'error':True}) # NOTE: 将error设置为True,
def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('Enter a sugject')

        if not request.POST.get('email',''):
            errors.append('Enter a email address')

        if not request.POST.get('message',''):
            errors.append('Enter a message')

        if not errors:
            return HttpResponseRedirect('/form/contact/thanks')

    return render(request,'contact_form.html',locals())

def thanks(request):
    return HttpResponse('thanks')


def formtest(request):
    if request.method == 'POST':
        form = RemarkForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print cd['subject']
            print cd['mail']
            print cd['topic']
            print cd['message']
            print cd['cc_myself']
            return HttpResponseRedirect('/form/form/')
    else:
        form = RemarkForm()
    return render(request,'formtest.html',{'form':form})

def form1test(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            dic = {'orderID':cd['orderID'],'title':cd['title'],'content':cd['content']}
            Adver.objects.create(**dic)
            return HttpResponseRedirect('/form/form1/')
    else:
        form = ContactForm()
    return render(request,'formtest1.html',{'form':form})
