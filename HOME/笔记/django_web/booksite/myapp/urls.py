#coding=utf-8
from django.conf.urls import *
from views import *

urlpatterns = patterns('',    #此处为空时,下面的视图函数,不需要加引号
    ('^model/$',model_fun),
    ('^base/$',base),
    ('^email/$',email)
)
