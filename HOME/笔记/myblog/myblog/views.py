#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    # return render(request,'blogapp.templates.base.html',{})
    return render(request,'base.html',{})
    # return HttpResponse('nihao')
