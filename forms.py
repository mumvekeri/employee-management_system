from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'first_name', 'last_name', 'job_title', 'job_grade', 'department',
            'branch', 'salary', 'cv', 'qualifications', 'contact_details', 
            'address', 'picture'
        ]
