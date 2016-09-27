from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=120, blank=False)
    image = models.FileField(null=True,blank=True,upload_to='cover/')
    order = models.CharField(max_length=15,blank=True)
    text = models.CharField(max_length=500,blank=True)
    featured = models.BooleanField(default = False)

 
    class Meta:
    	ordering = ["order"]

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id":self.id})

class CoverImage(models.Model):
    name = models.CharField(max_length=120, blank=False)
    image = models.FileField(null=True,blank=True,upload_to='cover/')
    featured = models.BooleanField(default = False)
    
    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id":self.id})

    def save(self, *args, **kwargs):
        if self.featured:
            CoverImage.objects.all().update(**{'featured': False})
        super(CoverImage, self).save(*args, **kwargs)

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

class CompanyAbout(models.Model):
    company_about = models.CharField(max_length=700)
    
    fb = models.BooleanField()
    fb_url = models.CharField(max_length=100)

    tw = models.BooleanField()
    tw_url = models.CharField(max_length=100)

    insta = models.BooleanField()
    insta_url = models.CharField(max_length=100)

    google_plus = models.BooleanField()
    google_url = models.CharField(max_length=100)

    pinterest = models.BooleanField()
    pinterest_url = models.CharField(max_length=100)