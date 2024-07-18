"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

<<<<<<< HEAD
from myApp.views import register, login, dashboard, prof, departments, correct
=======
from myApp.views import register, login, dashboard, prof, departments, correcr_attend
>>>>>>> af2ab45ffce76ec136c16655887f2a3c8998616b

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', register, name='register'),
    path('login/', login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('prof/', prof, name='prof'),
    path('departments/', departments, name='departments'),
<<<<<<< HEAD
    path('correct/', correct, name='correct')
    
=======
    path('correcr_attend/', correcr_attend, name='correcr_atttend')
>>>>>>> af2ab45ffce76ec136c16655887f2a3c8998616b
]
