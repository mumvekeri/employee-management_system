from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'templates/create_employee.html', {'form': form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'templates/employee_list.html', {'employees': employees})
