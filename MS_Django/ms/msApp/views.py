from email import message
from re import L
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import io

from django.http import FileResponse

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from django.core.mail import send_mail
from django.conf import settings



installed_apps =['msApp']

# Create your views here.
def index(request):
    if request.method == "POST":
        mes_name = request.POST['name']
        mes_email = request.POST['email']
        message = request.POST['message']

        #send an email
        send_mail(
            mes_name, #subject
            message, #message
            mes_email, #from email
            ['joycelyncorpuz28@gmail.com'], #to email
        )
        return render(request, 'msApp/index.html', {'mes_name':mes_name})
    else:
        return render(request, 'msApp/index.html',{})

def logins(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect ('msApp:attendance')
    if request.method == 'POST':
        users = request.POST.get('username')
        passw = request.POST.get('password') 
        request.session['username'] = users
        user = authenticate(request, username=users,password=passw)
 
        if user is not None:
            login(request, user)

            if user.is_staff:
                return redirect('msApp:attendance')
            else:
                messages.info(request,'Invalid Credentials!')
                return redirect('msApp:logins')

    form = CreateUserForm()
    if request.method == 'POST':
        email = request.POST["email"] # success email registration
        email=email # success email registration
        form = CreateUserForm(request.POST)
        messages.info(request,'Something went wrong!')
        form.instance.is_staff = True
        if form.is_valid():
            subject = 'Management System' # success email registration
            message = 'Welcome and Thank you for Registering in Management System.This is auto generated message.Do not reply...' # success email registration
            recipient = form.cleaned_data.get('email') # success email registration
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False) # success email registration
            messages.info(request,'Successfully Registered your Account!')
            form.save()
            return redirect('msApp:logins')

    return render(request, 'msApp/login.html')

def logina(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect ('msApp:homepage')
    if request.method == 'POST':
        users = request.POST.get('username')
        passw = request.POST.get('password') 
        request.session['username'] = users
        user = authenticate(request, username=users,password=passw)
 
        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('msApp:homepage')
            else:
                messages.info(request,'Invalid Credentials!')
                return redirect('msApp:logina')

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        messages.info(request,'Something went wrong!')
        form.instance.is_superuser = True
        if form.is_valid():
            messages.info(request,'Successfully Registered your Account!')
            form.save()
            return redirect('msApp:logina')

    return render(request, 'msApp/logina.html')

def functions(request):
    return render(request, 'msApp/functions.html')

@login_required(login_url='msApp:logins')
def attendance(request):
    if request.user.is_authenticated and request.user.is_staff:
        userData = request.user
        checkForm = User.objects.filter(username=userData).values()
        getDataAttendance = Attendance.objects.filter(username=userData)
        getRandomNum = request.POST.get('nums')
        attendance_del = Attendance.objects.filter(num=getRandomNum)
        payroll_del = Payroll.objects.filter(num=getRandomNum)

        list1 = []
        list2 = []

        for l in checkForm:
            list1.append(l)

        for a in getDataAttendance:
            list2.append(a)

        formattendance = AttendanceForm(request.POST or None)
        formpayroll = PayrollForm(request.POST or None)
        
        if request.method == 'POST':
            if formattendance.is_valid() and formpayroll.is_valid():
                messages.info(request,'Successfully Added the Attendance!')
                formattendance.save()
                formpayroll.save()
                return redirect('msApp:attendance')

        
        if request.method == "POST":
            messages.info(request,'Successfully Deleted!')
            attendance_del.delete()
            payroll_del.delete()
            return redirect('msApp:attendance')

        context = {
            'form': list1,
            'attendance': list2
        }
        return render(request, 'msApp/attendance.html', context)
    return redirect ('msApp:logins')

@login_required(login_url='msApp:logina')
def homepage(request):
    if request.user.is_authenticated:
        return render(request, 'msApp/homepage.html')
    return redirect ('msApp:logina')

@login_required(login_url='msApp:logina')
def payroll(request):
    if request.user.is_authenticated:
        getDataPayroll = Payroll.objects.all()

        context = {
            'payroll': getDataPayroll
        }
        return render(request, 'msApp/payroll.html', context)
    return redirect ('msApp:logina')

def pdf_generator(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 20)

    d1 = request.POST.get('employeeId') 
    d2 = request.POST.get('employeeName') 
    d3 = request.POST.get('employeeDate') 
    d4 = request.POST.get('employeeTime') 
    d5 = request.POST.get('employeeDeduction') 
    d6 = request.POST.get('employeeTotal')

    print(d1, d2, d3, d4, d5, d6)
    lines = [
        "Payroll Details:",
        "",
        d1,
        d2,
        d3,
        d4,
        d5,
        d6
    ]

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename="Payroll_Detail_for_"+d2+".pdf")

@login_required(login_url='msApp:logina')
def employee(request):
    if request.user.is_authenticated:
        getDataEmployee = Employee.objects.all()
        formemployee = EmployeeForm(request.POST or None)
        buy_id = request.POST.get('id')
        employee_del = Employee.objects.filter(id=buy_id)
        
        if request.method == 'POST':
            if formemployee.is_valid():
                messages.info(request,'Successfully Added the Employee!')
                formemployee.save()
                return redirect('msApp:employee')

        if request.method == "POST":
            messages.info(request,'Successfully Deleted!')
            employee_del.delete()
            return redirect('msApp:employee')

        context = {
            'employee': getDataEmployee
        }

        return render(request, 'msApp/employee.html', context)
    return redirect ('msApp:logina')

@login_required(login_url='msApp:logina')
def admin(request):
    if request.user.is_authenticated:
        getDataAdmin = User.objects.filter(is_superuser=True)

        admin_id = request.POST.get('id')
        admin_del = User.objects.filter(id=admin_id)

        if request.method == "POST":
            messages.info(request,'Successfully Deleted!')
            admin_del.delete()
            return redirect('msApp:admin')

        context = {
            "admin": getDataAdmin
        }
        return render(request, 'msApp/admin.html', context)
    return redirect ('msApp:logina')

@login_required(login_url='msApp:logina')
def logoutAdmin(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('msApp:logina')

@login_required(login_url='msApp:logina')
def users(request):
    if request.user.is_authenticated:
        getDataUser = User.objects.filter(is_staff=True)

        user_id = request.POST.get('id')
        user_del = User.objects.filter(id=user_id)

        if request.method == "POST":
            messages.info(request,'Successfully Deleted!')
            user_del.delete()
            return redirect('msApp:users')

        context = {
            "user": getDataUser
        }
        return render(request, 'msApp/users.html', context)
    return redirect ('msApp:logina')

@login_required(login_url='msApp:logins')
def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('msApp:logins')