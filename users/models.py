from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=500, unique=True)
    password= models.CharField(max_length=500)
    email= models.CharField(max_length=500, unique=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS= []
 







    
    
