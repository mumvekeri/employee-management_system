from django.urls import path
from .views import performance_management

urlpatterns = [
    path('', perfomance, name='perfomance'),
]
