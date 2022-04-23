from django.db import models

# Create your models here.
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