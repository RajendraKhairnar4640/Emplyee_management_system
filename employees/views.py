from django.shortcuts import render, redirect,get_object_or_404
from .models import Employee, Attendance
from .forms import EmployeeForm, AttendanceForm
from datetime import date
from django.db.models import Q

def dashboard(request):
    today = date.today()
    employee_count = Employee.objects.count()
    attendance = Attendance.objects.count()
    today_attendance_count = Attendance.objects.filter(date=today).count()
    context = {
        'employee_count': employee_count,
        'attendance':attendance,
        'today_attendance_count':today_attendance_count
    }
    return render(request, 'employees/dashboard.html',context)


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})


def edit_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_form.html', {'form': form})


def delete_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('employee_list')


def all_attendance(request):
    today = date.today()
    all_attendance = Attendance.objects.filter(~Q(date=today) | Q(date=today, is_present__isnull=False))
    return render(request, 'employees/all_attendance.html', {'all_attendance': all_attendance})


def today_attendance(request):
    today = date.today()
    
    today = date.today()
    employees = Employee.objects.all()
    attendance_records = Attendance.objects.filter(date=today)
    for employee in employees:
        attendance_exists = attendance_records.filter(employee=employee).exists()
        if not attendance_exists:
            Attendance.objects.create(employee=employee, date=today)
    today_attendance = Attendance.objects.filter(date=today)

    if today_attendance.exists():
        return render(request, 'employees/today_attendance.html', {'today_attendance': today_attendance})


def update_attendance(request, pk):
    attendance = Attendance.objects.get(pk=pk)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        
        if form.is_valid():
            # breakpoint()
            form.save()
            return redirect('today_attendance')
    form = AttendanceForm(instance=attendance, initial={'employee': attendance.employee, 'date': attendance.date})
    return render(request, 'employees/update_today_attendance.html', {'form': form})
