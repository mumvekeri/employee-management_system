from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('prof/', views.prof, name='prof'),
    path('departments/', views.departments, name='departments'),
    path('correct/', views.correct, name='correct'),
    path('performance/', views.performance, name='performance'),
    path('payroll/', views.payroll, name='payroll'),
]
