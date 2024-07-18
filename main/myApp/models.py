from django.db import models

# Create models here

class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    DEPARTMENT_CHOICES = [
        ('Engineering', 'Engineering'),
        ('Human Resources', 'Human Resources'),
        ('Finance', 'Finance'),
        ('Marketing', 'Marketing'),
        ('Operations', 'Operations'),
    ]

    fullname = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    cellphone_number = models.CharField(max_length=10)
    email = models.EmailField()
    job = models.CharField(max_length=100)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    date = models.DateField()
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return self.fullname
