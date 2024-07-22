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

from myApp.views import register, login, dashboard, prof, departments, correct, perfomance, payroll

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', register, name='register'),
    path('login/', login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('prof/', prof, name='prof'),
    path('departments/', departments, name='departments'),
    path('correct/', correct, name='correct'),
    path('perfomance/', perfomance, name='perfomance'),
    path('payroll/', payroll, name='payroll')
]
