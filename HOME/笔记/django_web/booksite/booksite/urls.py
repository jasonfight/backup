#coding=utf-8

from django.conf.urls import url,patterns,include
from django.contrib import admin
# from booksite.views import *# NOTE: 添加的信息,views需要创建

# # 新方法: 以列表的方式,必须通过引用来导入views文件
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url('^hello/$','hello'),      # NOTE: 将hello添加到url列表中
# ]
#
# urlpatterns += [url('^time/$','time'),
#                 url('^nihao/$','nihao'),
#                 url('^template/$','template_test'),
#                 ]


# #旧方法: 以函数的形式,可以不引用,而是通过函数的第一参数来导入views文件
urlpatterns = patterns('booksite.views',
    url(r'^admin/', admin.site.urls),
    ('^nihao/$','nihao'),
)
urlpatterns += patterns('booksite.views',
('^hello/$','hello'),
('^time/$','time'),
('^template/$','template_test'),
(r'^time/plus/(\d{1,2})/$','hours_ahead',{'m':'123'}),
)

urlpatterns += patterns('',
('^app/',include('myapp.urls')),
('^form/',include('formapp.urls')),
)

urlpatterns += patterns('',
('^login/',include('login_test_app.urls')),
)
