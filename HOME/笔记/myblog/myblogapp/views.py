from django.shortcuts import render
from django.http import HttpResponse

def nihao(request):
    return HttpResponse('nihao')
