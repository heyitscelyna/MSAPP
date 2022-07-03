from ast import mod
from django.db import models
import datetime
import os

# Create your models here.

# def filename(request, filename):
#     old_filename = filename
#     timenow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
#     filename = "%s%s", (timenow, old_filename)
#     return os.path.join('uploads/', filename)

# class admin(models.Model):
#     idno = models.CharField(max_length=15, null=False)
#     fullname = models.CharField(max_length=15, null=False)
#     username = models.CharField(max_length=15, null=False)

class Employee(models.Model):
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)


class Attendance(models.Model):
    dates = models.DateField()
    employee = models.CharField(max_length=100)
    timein = models.TimeField()
    timeout = models.TimeField()
    username = models.CharField(max_length=100)
    totalrecord = models.CharField(max_length=100)
    num = models.IntegerField()

class Payroll(models.Model):
    employee = models.CharField(max_length=100)
    total = models.IntegerField()
    num = models.IntegerField()
    totalrecord = models.CharField(max_length=100)
    dates = models.DateField()