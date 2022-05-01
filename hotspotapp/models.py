from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from phone_field import PhoneField

# Create your models here.
class Profile(models.Model):
        user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        profile_image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
        about = models.CharField(max_length=400)
        company = models.CharField(max_length=200)
        job = models.CharField(max_length=200)
        country = CountryField()
        address = models.CharField(max_length=300)
        phone = PhoneField(blank=True, help_text='Contact phone number')
        twitter_url = models.URLField()
        facebook_url = models.URLField()
        instagram_url = models.URLField()
        linkedin_url = models.URLField()
        
        class meta:
            exclude = ['user']
            
        def __unicode__(self):
            return self.job
        
        

class Artist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    location = models.CharField(max_length=100)

    class Meta:
        managed = True
        verbose_name = 'Artist'
        verbose_name_plural = 'Artist'
        
    def __str__(self):
        return self.first_name



class Producer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    location = models.CharField(max_length=100)

    class Meta:
        managed = True
        verbose_name = 'Producer'
        verbose_name_plural = 'Producer'
        
    def __str__(self):
        return self.first_name
    

class Commedian(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    location = models.CharField(max_length=100)

    class Meta:
        managed = True
        verbose_name = 'Commedian'
        verbose_name_plural = 'Commedian'
        
    def __str__(self):
        return self.first_name
        
class Dj(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    location = models.CharField(max_length=100)

    class Meta:
        managed = True
        verbose_name = 'Dj'
        verbose_name_plural = 'Dj'
        
    def __str__(self):
        return self.first_name