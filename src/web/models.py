from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=120, blank=False)
    image = models.FileField(null=True,blank=True)
    order = models.CharField(max_length=15,blank=True)
    text = models.CharField(max_length=500,blank=True)
 

    class Meta:
    	ordering = ["order"]


    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id":self.id})

class CoverImage(models.Model):
    name = models.CharField(max_length=120, blank=False)
    image = models.FileField(null=True,blank=True,upload_to='cover/')
    order = models.CharField(max_length=15,blank=True)
    text = models.CharField(max_length=100,blank=True)

    
    class Meta:
    	ordering = ["order"]

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id":self.id})


class Client(models.Model):
    name  = models.CharField(max_length=100,blank=True)
    image = models.FileField(null=True,blank=True,upload_to='client/')
    order = models.CharField(max_length=15,blank=True)

    class Meta:
        ordering = ["order"]

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id":self.id})
