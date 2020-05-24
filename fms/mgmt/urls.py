
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[

     path('',views.home,name='home'),
     path('login',views.login,name='login'),
     path('logout',views.logout,name='logout'),
     path('addincome',views.addincome,name='addincome'),
     path('add',views.add,name='add'),
     path('spendmoney',views.spendmoney,name='spendmoney'),
     path('formoney',views.formoney,name='formoney'),
     path('newaddincome',views.newaddincome,name='newaddincome'),



     path('nextaddmoney',views.nextaddmoney,name='nextaddmoney'),
     path('formoney1',views.formoney1,name='formoney1'),
     
     path('register',views.register,name='register'),

     
  
     path('addspending',views.addspending,name='addspending'),
     
     path('income',views.income,name='income'),
     
     path('morespending',views.morespending,name='morespending'),
     path('totalincomes',views.totalincomes,name='totalincomes'),
     
   


    
]