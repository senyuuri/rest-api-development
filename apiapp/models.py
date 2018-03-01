import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Diary(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=True, max_length=100)
    author = models.ForeignKey('auth.User', related_name='diary', on_delete=models.CASCADE)
    publish_date = models.DateTimeField('Publish Date', auto_now_add=True)
    public = models.BooleanField(default=True)
    text = models.CharField(blank=True, max_length=10000)


class Profile(models.Model):
    """Extend django's native User model to store custom profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(default='', max_length=50)
    age = models.IntegerField(default=0)


class UserToken(models.Model):
    user = models.ForeignKey('auth.user', related_name='token', on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4(), editable=False, primary_key=True)
