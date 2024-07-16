from django.shortcuts import render


def register(request):
    return render(request, 'register.html', {})
def login(request):
    return render(request, 'login.html', {})
def dashboard(request):
    return render(request, 'dashboard.html', {}) 
def prof(request):
    return render(request, 'prof.html', {}) 
def departments(request):
    return render(request, 'departments.html', {})