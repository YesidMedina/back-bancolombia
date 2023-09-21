# from django.contrib import admin
# from .models import UsersModel

# admin.site.register(UsersModel)

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
