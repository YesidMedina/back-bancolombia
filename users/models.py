from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    customer_id = models.CharField(max_length=500, blank=True, null=True)
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'









# from django.db import models

# class UsersModel(models.Model):
#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)
#     status = models.CharField(max_length=20)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
        
#     class Meta:
#         db_table = 'users'
#         ordering = ['-created_at']
    
    
    
    # from django.db import models

# class UsersModel(models.Model):
    
#     password = models.CharField(max_length=20)
#     last_login = models.DateTimeField(auto_now_add=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField(auto_now_add=True)
    
    
#     class Meta:
#         db_table = 'auth_user'
#         ordering = ['-last_login']
    
    
    
    
    
    
    
    
