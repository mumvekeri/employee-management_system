from django.urls import path

from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('', register, name='register'),
    path('', login, name='login'),
    path('', dashboard, name='dashboard')
]