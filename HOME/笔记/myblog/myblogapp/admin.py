#coding=utf-8
from django.contrib import admin
from myblogapp.models import *


class BlogAdadmin(admin.ModelAdmin):
    list_display = ('index','title','date_publish','description','callback_url') # NOTE: 在admin中显示相应的列
    search_fields = ('date_publish','index','title')    # NOTE: 可通过相应的列查询

class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ('title','desc','click_count','is_recommend','date_publish','user')

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','index')

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('username','email',)




admin.site.register(BlogAd,BlogAdadmin)
admin.site.register(BlogArticle,BlogArticleAdmin)
admin.site.register(BlogCategory,BlogCategoryAdmin)
admin.site.register(BlogComment)
admin.site.register(BlogLinks)
admin.site.register(BlogTag)
admin.site.register(BlogUser)




# class BlogArticle(models.Model):
#
#
#
# class BlogArticleTag(models.Model):
#
#
#
# class BlogCategory(models.Model):
#
#
#
# class BlogComment(models.Model):
#
#
# class BlogLinks(models.Model):
#
#
#
# class BlogTag(models.Model):
#
#
# class BlogUser(models.Model):
#
#
# class BlogUserGroups(models.Model):
#
