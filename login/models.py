from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    
    ###status of the advertisement	
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Access(models.Model):
	print 'model access'
	print '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
	name=models.CharField(max_length=200)
	phone=models.CharField(max_length=200)
	ip=models.CharField(max_length=200)
	mac=models.CharField(max_length=200)
	OTP=models.CharField(max_length=4)
	
	def __self__(self):
		return self.name
	def __unicode__(self):
      	        return  self.mac
