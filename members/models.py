from msilib.schema import Class
from optparse import TitledHelpFormatter
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User



class user(models.Model):
    firstname = models.CharField(max_length=101)
    lastname = models.CharField(max_length=101)
    email = models.EmailField()
    username = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    image= models.ImageField(null=True ,upload_to='profile')
    gender= models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    reg_date = models.DateTimeField(auto_now_add=True)

    


# Create your models here.
class Members(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)

class movies(models.Model):
  title = models.CharField(max_length=255)
  #released_date= models.CharField(max_length=255)
  main_actor = models.CharField(max_length=255)
  genre=(
      ('action','ACTION'),
      ('comedy','COMEDY'),
      ('music','MUSIC'),
  )
  genre =  models.CharField(max_length=255,choices=genre)
  descripltion = models.CharField(max_length=255)
  video = models.FileField(upload_to='media',
  validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
  thumbnail = models.ImageField(upload_to='thumbnail')
  url = models.CharField(max_length=255)
  user_id = models.CharField(max_length=255)
      

