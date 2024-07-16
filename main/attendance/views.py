from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import Attendance, Employee

@method_decorator(csrf_exempt, name='dispatch')
def attendance_list(request):
    if request.method == 'GET':
        attendances = Attendance.objects.all()
        data = [{"date": a.date, "employee": a.employee.name, "check_in_time": a.check_in_time, "check_out_time": a.check_out_time, "status": a.status} for a in attendances]
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        employee = Employee.objects.get(id=data['employee_id'])
        attendance = Attendance.objects.create(
            date=data['date'],
            employee=employee,
            check_in_time=data['check_in_time'],
            check_out_time=data['check_out_time'],
            status=data['status']
        )
        return JsonResponse({"message": "Attendance added successfully"}, status=201)

@method_decorator(csrf_exempt, name='dispatch')
def employee_list(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        data = [{"id": e.id, "name": e.name, "position": e.position, "date_joined": e.date_joined} for e in employees]
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        employee = Employee.objects.create(
            name=data['name'],
            position=data['position'],
            date_joined=data['date_joined']
        )
        return JsonResponse({"message": "Employee added successfully"}, status=201)
