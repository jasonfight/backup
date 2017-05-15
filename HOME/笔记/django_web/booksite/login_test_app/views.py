#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from models import *
# Create your views here.


def login(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('account',''):
            errors.append('Enter a sugject')

        if not request.POST.get('password',''):
            errors.append('Enter a email address')

        if not errors:
            return HttpResponse('thanks')
            # return HttpResponseRedirect('/login/thanks')
        
    return render(request,'login.html',locals())

# def thanks(request):
#     return HttpResponse('thanks')
def register(request):
    pass
