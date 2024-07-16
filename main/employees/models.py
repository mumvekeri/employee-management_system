from django.db import models

class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    initials = models.CharField(max_length=10)
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    cell_number = models.CharField(max_length=15)
    email = models.EmailField()
    date_joined = models.DateField()
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True)
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)

    def __str__(self):
        return self.full_name
