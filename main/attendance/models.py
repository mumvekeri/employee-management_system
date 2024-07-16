from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date_joined = models.DateField()

    def __str__(self):
        return self.name

class Attendance(models.Model):
    date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.employee.name} - {self.date}"
