from unicodedata import name
from django.urls import path
from django.conf import settings
from . import views

app_name = 'msApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('login/', views.logins, name='logins'),
    path('logina/', views.logina, name='logina'),
    path('functions/', views.functions, name='functions'),
    path('attendance/', views.attendance, name='attendance'),
    path('employee/', views.employee, name='employee'),
    path('homepage/', views.homepage, name='homepage'),
    path('admin/', views.admin, name='admin'),
    path('users/', views.users, name='users'),
    path('payroll/', views.payroll, name='payroll'),
    path('logoutAdmin/', views.logoutAdmin, name="logout"),
    path('logoutUser/', views.logoutUser, name="logoutu"),
    path('pdf_generator/', views.pdf_generator, name="pdf_generator")

]