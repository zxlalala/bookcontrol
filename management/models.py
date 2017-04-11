from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    price = models.FloatField()
    publish_date = models.DateField()
    # category = models.CharField(max_length=128)

    def __unicode__(self):
        return self.title

    class META:
        ordering = ['title']

class MyUser(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=128)
    permission = models.IntegerField(default=1)

    def __unicode__(self):
        return self.user.username
