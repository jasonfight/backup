#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
from datetime import *
from django.core.mail import send_mail
# Create your views here.


def base(request):
    return render(request,'base.html',{})

def email(request):
    send_mail('django email','send email test','guohao0221@126.com',['guohao0221@126.com'])
    return HttpResponse('send ok')





def model_fun(request):
    count = Book.objects.title_count('shoot-skill')
    return render(request,'model.html',locals())

    # 增加
    # Publisher.objects.create(name = 'jason.ltd',address = 'First Street',city = 'XIAN',state_province = 'SHAANXI',country = 'China',website = 'www.baidu.com')
    #
    # dic = {'first_name':'Hao','last_name':'Guo','email':'guohao@126.com'}
    # Author.objects.create(**dic)
    #
    # obj = Book(title = 'basketballskill',publication_date = datetime.now(),publisher_id = 2)
    # obj.save()
    # # 删除
    # Publisher.objects.filter(id = 2).delete()

    # # 改
    # Author.objects.filter(id=2).update(first_name = 'miao',last_name = 'zhang')
    #
    # obj = Book.objects.get(id=3)
    # obj.title = 'shootskill'
    # obj.save()

    # # 查
    # book = Book.objects.all()
    #
    # a = Publisher.objects.all().values('name')
    # b = Author.objects.get(id = 1)
    #
    # c = Publisher.objects.filter(id__gt=0).count()
    #
    # return render(request,'model.html',locals())
