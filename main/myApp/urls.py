from django.urls import path
from .views import get_total_employees

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('prof/', views.prof, name='prof'),
    path('departments/', views.departments, name='departments'),
    path('correct/', views.correct, name='correct'),
    path('perfomance/', views.perfomance, name='perfomance'),
    path('payroll/', views.payroll, name='payroll'),
    path('api/total-employees/', get_total_employees, name='total_employees'),
]
