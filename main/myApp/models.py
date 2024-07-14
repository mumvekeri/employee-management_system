from django.db import models

# Create your models here.

class Employee(models.Model):
    initials = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    cell_number = models.CharField(max_length=20)
    email = models.EmailField()
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    date_joined = models.DateField()
    picture = models.ImageField(upload_to='employee_pics/')
    cv = models.FileField(upload_to='employee_cvs/')

