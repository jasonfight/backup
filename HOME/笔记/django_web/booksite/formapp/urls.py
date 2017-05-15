
#coding=utf-8
from django.conf.urls import *
from views import *


urlpatterns = patterns('',    #此处为空时,下面的视图函数,不需要加引号
    ('^search-form/$',search_form),
    ('^search/$',search)
)
urlpatterns += patterns('',
    ('^contact/$',contact),
    ('^contact/thanks/$',thanks),
)
urlpatterns += patterns('',
    ('^form/$',formtest),
    ('^form1/$',form1test),
)
