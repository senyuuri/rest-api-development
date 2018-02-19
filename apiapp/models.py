import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Diary(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=True, max_length=100)
    author = models.ForeignKey('auth.User', related_name='diary', on_delete=models.CASCADE)
    publish_date = models.DateTimeField('Publish Date')
    public = models.BooleanField(default=True)
    text = models.CharField(blank=True, max_length=10000)


class Profile(models.Model):
    """Extend django's native User model to store custom profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(default='', max_length=50)
    age = models.IntegerField(default=0)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create profile for newly registered user"""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save user profile"""
    instance.profile.save()