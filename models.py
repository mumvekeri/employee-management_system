from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    job_grade = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    cv = models.FileField(upload_to='cvs/')
    qualifications = models.TextField()
    contact_details = models.TextField()
    address = models.TextField()
    picture = models.ImageField(upload_to='pictures/', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
