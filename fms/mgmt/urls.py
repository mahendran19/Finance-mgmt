
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[

     path('',views.home,name='home'),
     path('serial',views.serial,name='serial'),
     path('register',views.register,name='register'),
     path('income',views.income,name='income'),
     path('spendmoney',views.spendmoney,name='spendmoney'),
     path('totalincomes',views.totalincomes,name='totalincomes'),
     path('add',views.add,name='add'),
     path('formoney',views.formoney,name='formoney'),
     path('login',views.login,name='login'),
     path('logout',views.logout,name='logout')


    
]