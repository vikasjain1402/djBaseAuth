from django.db import models

from django.contrib.auth.models import AbstractUser

#User._meta.get_field('email')._unique=True
class Profile (AbstractUser):
    fathername=models.CharField(max_length=100, blank=True, null=True)
    dateofbirth=models.DateField(blank=True,null=True)
    profilepic=models.ImageField(upload_to='media/images',null=True,blank=True)