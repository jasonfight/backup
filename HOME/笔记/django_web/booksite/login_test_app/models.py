from __future__ import unicode_literals

from django.db import models

# Create your models here.

class LoginTest_User(models.Model):
    account = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    tel = models.CharField(max_length=15)

    def __unicode__(self):
        return self.account
    class Meta:
        verbose_name = "login_user"
        ordering = ['account']
