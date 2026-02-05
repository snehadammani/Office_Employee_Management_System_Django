from django.shortcuts import render,HttpResponse
from .models import Employees,Role,Department
from datetime import datetime
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,'index.html')
def all_emp(request):
    emps = Employees.objects.all()
    context ={
        'emps':emps

    }
    print(context)
    return render(request,'view_all_emp.html',context)
def add_emp(request):
    if request.method=="POST":
        first_name = request.POST.get('first_name','').strip()
        last_name = request.POST.get('last_name','').strip()
        salary = int(request.POST.get('salary',0))
        bonus = int(request.POST.get('bonus',0))
        phone = int(request.POST.get('phone',0))
        dept_id= request.POST.get('dept')
        role_id = request.POST.get('role')

        if not dept_id or not role_id:
            return HttpResponse("Please select both Department and Role")
        new_emp=Employees(
            first_name=first_name,
            last_name=last_name,
            salary=salary,
            bonus=bonus,
            phone=phone,
            dept_id=int(dept_id),
            role_id=int(role_id),
            hire_date=datetime.now()
        )
        new_emp.save()
        return HttpResponse('Employee added Sucessful')
    depts = Department.objects.all()
    roles = Role.objects.all()

    return render(request,'add_emp.html',{
        'depts':depts,
        'roles':roles
    })
    
    #elif request.method == 'GET':
     #   return render(request,'add_emp.html')
    #else:
     #   return HttpResponse('An Exception Occured Employee is ')
def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employees.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please enter a valid emp id:")
    emps=Employees.objects.all()
    context={
        'emps':'emps'
    }
    return render(request,'remove_emp.html',context)
def filter_emp(request):
    if request.method =="Post":
        name = request.Post['name']
        dept = request.Post['dept']
        role_id = request.Post['role_id']
        emps = Employees.object.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name= dept)
        if role_id:
            emps=emps.filter(role_id__name=role)
        context = {
            'emps':emps
        }
        return render(request,'view_all_emp.html',context)
    elif request.method == 'GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse('An Exception Occured')