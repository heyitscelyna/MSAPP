from dataclasses import field, fields
from pyexpat import model
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','username', 'password1', 'password2','email']


class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = '__all__'
		

class AttendanceForm(forms.ModelForm):
	class Meta:
		model = Attendance
		fields = '__all__'

class PayrollForm(forms.ModelForm):
	class Meta:
		model = Payroll
		fields = '__all__'