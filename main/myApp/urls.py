from django.urls import path

from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('', register, name='register'),
    path('', login, name='login'),
    path('', dashboard, name='dashboard'),
    path('', prof, name='prof'),
    path('', departments, name='departments'),
    path('',correcr_attend, name='correcr_attend.html')
    ]