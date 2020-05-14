
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[

     path('',views.home,name='home'),

     path('register',views.register,name='register'),
     path('income',views.income,name='income'),
     path('add',views.add,name='add'),
     path('login',views.login,name='login'),
     path('logout',views.logout,name='logout')


    
]