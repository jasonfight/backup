#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class BookManager(models.Manager):
#     def title_count(self,keyword):
#         return self.filter(title__icontains = keyword).count()

class User(AbstractUser):
    # avater = models.ImageField()
    mobile = models.CharField(max_length=20,blank = True,null = True)
    class Meta:
        verbose_name = "User"
        ordering = ['-id']
    def __unicode__(self):
        return self.username

class Publisher(models.Model):      # NOTE: 使用类的方式,来建立数据库表格
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length =50)
    city =  models.CharField(max_length =60)
    state_province =  models.CharField(max_length =30)
    country =  models.CharField(max_length =50)
    website = models.URLField()
    def __unicode__(self):
        return self.name  # NOTE: 在admin网页中,显示name而不是类型
    class Meta:             # NOTE: 在admin网页中,显示的名称为 publishers
        verbose_name = "publisher"
        ordering = ['name']


class Author(models.Model):
    first_name =  models.CharField(max_length =30)
    last_name =  models.CharField(max_length =30)
    email = models.EmailField(blank = True,verbose_name = 'e-mail')
    def __unicode__(self):
        return u'%s %s'%(self.first_name,self.last_name)
    class Meta:
        verbose_name = 'Auther'
        ordering = ['first_name']

class Book(models.Model):
    title =  models.CharField(max_length =100)
    publication_date = models.DateField(blank = True,null = True)
    publisher = models.ForeignKey(Publisher)
    author = models.ManyToManyField(Author)
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = 'Book'
        ordering = ['id']
