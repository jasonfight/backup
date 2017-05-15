#coding=utf-8
from __future__ import unicode_literals

from django.db import models



class BlogAd(models.Model):
    title = models.CharField(max_length=50,verbose_name = '标题')
    description = models.CharField(max_length=200,verbose_name = '描述')
    image_url = models.CharField(max_length=100,verbose_name = '图像地址')
    callback_url = models.CharField(max_length=200, blank=True, null=True,verbose_name = '网址')
    date_publish = models.DateTimeField(verbose_name = '时间')
    index = models.IntegerField(verbose_name = '索引')

    class Meta:
        managed = False
        db_table = 'blog_ad'
        verbose_name = '广告'
    def __unicode__(self):
        return self.title

class BlogArticle(models.Model):
    title = models.CharField(max_length=50,verbose_name = '标题')
    desc = models.CharField(max_length=50,verbose_name = '描述')
    content = models.TextField(verbose_name = '内容')
    click_count = models.IntegerField(verbose_name = '点击量')
    is_recommend = models.IntegerField(verbose_name = '评论回复数量')
    date_publish = models.DateTimeField(verbose_name = '出版日期')
    category = models.ForeignKey('BlogCategory', models.DO_NOTHING, blank=True, null=True,verbose_name = '类别')
    user = models.ForeignKey('BlogUser', models.DO_NOTHING,verbose_name = '用户')

    class Meta:
        managed = False
        db_table = 'blog_article'
        verbose_name = '文章'
    def __unicode__(self):
        return self.title


class BlogCategory(models.Model):
    name = models.CharField(max_length=30,verbose_name = '名称')
    index = models.IntegerField(verbose_name = '索引')

    class Meta:
        managed = False
        db_table = 'blog_category'
        verbose_name = '类别'
    def __unicode__(self):
        return self.name

class BlogComment(models.Model):
    content = models.TextField()
    username = models.CharField(max_length=30, blank=True, null=True,verbose_name = '用户名')
    email = models.CharField(max_length=50, blank=True, null=True,verbose_name = '邮箱')
    url = models.CharField(max_length=100, blank=True, null=True,verbose_name = '网址')
    date_publish = models.DateTimeField(verbose_name = '出版日期')
    article = models.ForeignKey(BlogArticle, models.DO_NOTHING, blank=True, null=True,verbose_name = '文章')
    pid = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True,verbose_name = 'PID')
    user = models.ForeignKey('BlogUser', models.DO_NOTHING, blank=True, null=True,verbose_name = '用户')

    class Meta:
        managed = False
        db_table = 'blog_comment'
        verbose_name = '评论'
    def __unicode__(self):
        return self.username

class BlogLinks(models.Model):
    title = models.CharField(max_length=50,verbose_name = '标题')
    description = models.CharField(max_length=200,verbose_name = '简介')
    callback_url = models.CharField(max_length=200,verbose_name = '带更改')
    date_publish = models.DateTimeField(verbose_name = '出版日期')
    index = models.IntegerField(verbose_name = '索引')

    class Meta:
        managed = False
        db_table = 'blog_links'
        verbose_name = '链接'
    def __unicode__(self):
        return self.title

class BlogTag(models.Model):
    name = models.CharField(max_length=30,verbose_name = '名称')

    class Meta:
        managed = False
        db_table = 'blog_tag'
        verbose_name = '标签'
    def __unicode__(self):
        return self.name

class BlogUser(models.Model):
    password = models.CharField(max_length=128,verbose_name = '密码')
    last_login = models.DateTimeField(blank=True, null=True,verbose_name = '上次登录时间')
    is_superuser = models.IntegerField(verbose_name = '是否为超级用户')
    username = models.CharField(unique=True, max_length=30,verbose_name = '用户名')
    first_name = models.CharField(max_length=30,verbose_name = '名')
    last_name = models.CharField(max_length=30,verbose_name = '姓')
    email = models.CharField(max_length=254,verbose_name = '邮箱')
    is_staff = models.IntegerField(verbose_name = '是否为工作人员')
    is_active = models.IntegerField(verbose_name = '是否活跃')
    date_joined = models.DateTimeField(verbose_name = '注册日期')
    avatar = models.CharField(max_length=200, blank=True, null=True,verbose_name = '头像')
    qq = models.CharField(max_length=20, blank=True, null=True,verbose_name = 'QQ')
    mobile = models.CharField(unique=True, max_length=11, blank=True, null=True,verbose_name = '电话')
    url = models.CharField(max_length=100, blank=True, null=True,verbose_name = '地址')

    class Meta:
        managed = False
        db_table = 'blog_user'
        verbose_name = '博客用户'
    def __unicode__(self):
        return self.username


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=80)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'

# class BlogArticleTag(models.Model):
#     article = models.ForeignKey(BlogArticle, models.DO_NOTHING)
#     tag = models.ForeignKey('BlogTag', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'blog_article_tag'
#         unique_together = (('article', 'tag'),)
#         verbose_name = '标签'
#     def __unicode__(self):
#         return self.aiticle
# class BlogUserGroups(models.Model):
#     user = models.ForeignKey(BlogUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'blog_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
#
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=30)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)




# class BlogUserUserPermissions(models.Model):
#     user = models.ForeignKey(BlogUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'blog_user_user_permissions'
#         unique_together = (('user', 'permission'),)
#
#
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(BlogUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'

#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'
