"""
URL configuration for master_file project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.urls import url_users
from amm_im.urls import url_amm_im
from amm_apm.urls import url_amm_apm
from amm_cloud.urls import url_amm_cloud
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(url_users)),
    path('api/generate_token', views.obtain_auth_token),
    path('api/', include(url_amm_im)),
    path('api/', include(url_amm_apm)),
    path('api/', include(url_amm_cloud))
    
]
