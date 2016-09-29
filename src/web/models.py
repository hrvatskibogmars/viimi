from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from tinymce.models import HTMLField


class Project(models.Model):
    name = models.CharField(max_length=120, blank=False)
    image = models.FileField(null=True,blank=True,upload_to='cover/')
    order = models.CharField(max_length=15,blank=True)
    text = HTMLField(max_length=500,blank=True)
    featured = models.BooleanField(default = False)
 
    class Meta:
    	ordering = ["order"]
        verbose_name = '3. Projects'
        verbose_name_plural = '3. Projects'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id":self.id})

class CoverImage(models.Model):
    name = models.CharField(max_length=120, blank=False)
    image = models.FileField(null=True,blank=True,upload_to='cover/')
    featured = models.BooleanField(default = False)
    
    class Meta:
        verbose_name = '1. Home'
        verbose_name_plural = '1. Home'
    
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
        verbose_name = '5. Client'
        verbose_name_plural = '5. Clients'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id":self.id})

class OurServices(models.Model):
    text = HTMLField(max_length=10000,blank=True)
    featured = models.BooleanField(default = False)
    name  = models.CharField(max_length=100,blank=True)
    
    class Meta:
        verbose_name = '2. Services'
        verbose_name_plural = '2. Services'
    
    def __unicode__(self):
        return self.name            

class AboutUs(models.Model):
    keith_text = HTMLField(max_length=10000,blank=True)
    keith_cv =models.FileField(null=True,blank=True,upload_to='cv/')
    keith_image = models.FileField(null=True,blank=True,upload_to='about/')
    keith_image_2 = models.FileField(null=True,blank=True,upload_to='about/')

    izabela_text = HTMLField(max_length=10000, blank=True)
    izabela_cv =models.FileField(null=True,blank=True,upload_to='cv/')
    izabela_image = models.FileField(null=True,blank=True,upload_to='about/')
    izabela_image_2 = models.FileField(null=True,blank=True,upload_to='about/')


    def __unicode__(self):
        return "About us"    
    class Meta:
        verbose_name = '4. About Us'
        verbose_name_plural = '4. About Us'      
