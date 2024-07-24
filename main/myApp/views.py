from django.http import JsonResponse
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
def correct(request):
    return render(request, 'correct.html', {})
def perfomance(request):
    return render(request, 'perfomance.html', {})
def payroll(request):
    if request.method == 'POST':
        employee_id = request.POST['employeeIdProcessing']
        month = request.POST['month']
        gross_pay = float(request.POST['grossPay'])
        total_deductions = float(request.POST['totalDeductions'])
        total_bonuses = float(request.POST['totalBonuses'])
        total_fringe_benefits = float(request.POST['totalFringeBenefits'])
        net_pay = float(request.POST['netPayProcessing'])

        employee = Employee.objects.get(id=employee_id)

        payroll_entry = Payroll(
            employee=employee,
            month=month,
            gross_pay=gross_pay,
            total_deductions=total_deductions,
            total_bonuses=total_bonuses,
            total_fringe_benefits=total_fringe_benefits,
            net_pay=net_pay
        )
        payroll_entry.save()
        

        return JsonResponse({'message': 'Payroll processed successfully.'})
    return render(request, 'payroll.html', {})

def get_total_employees(request):
    total_employees = Employee.objects.count()
    return JsonResponse({'total_employees': total_employees})

