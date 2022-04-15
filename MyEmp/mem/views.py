from datetime import datetime
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from django.contrib import messages
from .models import Contact, Department, Employee, Role
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'mem/index.html')

def about(request):
    return render(request,'mem/about.html')

def allEmp(request):
    emps = Employee.objects.all()
    context = {'emps':emps}
    return render(request,'mem/allEmp.html',context)

def addEmp(request):
    deps = Department.objects.all()
    rols = Role.objects.all()
    context = {'deps':deps,'rols':rols}
    if request.method == "POST":
        firstName = request.POST.get('firstName','')
        lastName = request.POST.get('lastName', '')
        dept = request.POST.get('dept', '')
        salary = request.POST.get('salary', '')
        bonus = request.POST.get('bonus', '')
        role = request.POST.get('role', '')
        phone = request.POST.get('phone', '')
        hiredate = request.POST.get('hiredate', '')
        addEmp = Employee(firstName=firstName, lastName=lastName, dept_id=dept, salary=salary, bonus=bonus, role_id=role, phone=phone, hiredate=hiredate)
        addEmp.save()
        messages.success(request, "Employee has been successfully added!")

    return render(request,'mem/addEmp.html',context)

def remEmp(request,emp_id=0):
    if emp_id:
        try:
            emp_be_removed = Employee.objects.get(id = emp_id)
            emp_be_removed.delete()
            messages.success(request, "Employee has been successfully removed!")

        except:
            messages.warning(request, "Something error ocurred please try again later!")

    emps = Employee.objects.all()
    context = {'emps':emps}
    return render(request,'mem/remEmp.html',context)

def findEmp(request):
    emps = Employee.objects.all()
    if request.method == 'POST':
        firstName = request.POST.get('firstName','')
        dept = request.POST.get('dept', '')
        role = request.POST.get('role', '')
        if firstName:
            emps = emps.filter(Q(firstName__icontains = firstName) | Q(lastName__icontains = firstName))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)
        context = {'emps':emps}
        return render(request,'mem/allEmp.html',context)
    elif request.method == 'GET':
        return render(request,'mem/findEmp.html')
    else:
        messages.warning(request, "An error occured!")
        return render(request,'mem/findEmp.html')
            
            
def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
        messages.success(request, "Your query has been successfully submited. We will get touh with you soon.")
    return render(request, 'mem/contact.html', {'thank': thank})