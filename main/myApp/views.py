from django.shortcuts import render
from .models import Employee


def register(request):
    return render(request, 'register.html', {})
def login(request):
    return render(request, 'login.html', {})
def dashboard(request):
    return render(request, 'dashboard.html', {}) 
def prof(request):
    if request.method=="POST":
        fullname=request.POST['fullname']
        gender=request.POST['gender']
        age=request.POST['age']
        cellphone_number=request.POST['cellphone_number']
        email=request.POST['emial']
        job=request.POST['job']
        department=request.POST['department']
        date=request.POST['date']
        picture=request.POST['picture']
        files=request.POST['files']
        Employee=Employee(fullname=fullname,gender=gender,Age=age,cellphone_number=cellphone_number,email=email,job=job,department=department,date=date,picture=picture,files=files)
        Employee.save()
    
    return render(request, 'prof.html', {}) 
def departments(request):
    return render(request, 'departments.html', {})
def correcr_attend(request):
    return render(request, 'correcr_attend', {})