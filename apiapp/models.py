from django.db import models

# Create your models here.
class Diary(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(blank=True, max_length=100)
	publish_date = models.DateTimeField('Publish Date')
	public = models.BooleanField(default=True)
	text = models.CharField(blank=True, max_length=10000)