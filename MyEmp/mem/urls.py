from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='MemHome'),
    path('about/', views.about,name='MemAbout'),
    path('contact/', views.contact,name='MemContact'),
    path('allEmp/', views.allEmp,name='AllEmp'),
    path('remEmp/', views.remEmp,name='RemEmp'),
    path('remEmp/<int:emp_id>', views.remEmp,name='RemEmp'),
    path('addEmp/', views.addEmp,name='AddEmp'),
    path('findEmp/', views.findEmp,name='FindEmp'),
]