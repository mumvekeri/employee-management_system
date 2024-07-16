from django.urls import path
from .views import attendance_list, employee_list

urlpatterns = [
    path('attendances/', attendance_list, name='attendance_list'),
    path('employees/', employee_list, name='employee_list'),
]
