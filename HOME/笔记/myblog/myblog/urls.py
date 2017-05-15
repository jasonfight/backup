#coding=utf-8
from django.conf.urls import url,include
from django.contrib import admin
from views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$',homepage),
]
urlpatterns += [
    url('^',include('myblogapp.urls')),
]
