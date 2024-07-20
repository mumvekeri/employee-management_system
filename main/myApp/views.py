from django.shortcuts import render
from .models import Employee

def register(request):
    return render(request, 'register.html', {})

def login(request):
    return render(request, 'login.html', {})

def dashboard(request):
    return render(request, 'dashboard.html', {}) 

def prof(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        gender = request.POST['gender']
        age = request.POST['age']
        cellphone_number = request.POST['cellphone_number']
        email = request.POST['email']  # Corrected typo
        job = request.POST['job']
        department = request.POST['department']
        date = request.POST['date']
        picture = request.FILES.get('picture')  # Correctly handle file uploads
        files = request.FILES.get('files')  # Correctly handle file uploads
        
        # Create a new Employee instance and save it
        employee = Employee(
            full_name=fullname,
            gender=gender,
            age=age,
            cellphone_number=cellphone_number,
            email=email,
            job=job,
            department=department,
            date=date,
            picture=picture,
            documents=files  # Assuming 'files' is meant to be 'documents'
        )
        employee.save()
    
    return render(request, 'prof.html', {})

def departments(request):
    return render(request, 'departments.html', {})

def correcr_attend(request):
    return render(request, 'correcr_attend.html', {})  # Corrected typo in file name
