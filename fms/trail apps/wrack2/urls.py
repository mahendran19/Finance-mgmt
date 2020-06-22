from django.contrib import admin
from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('income',views.income,name='income'),
    path('adding',views.adding,name='adding'),
    path('addincome',views.addincome,name='addincome'),
    path('add2',views.add2,name='add2'),
    path('spendmoney',views.spendmoney,name='spendmoney'),
    path('addspending',views.addspending,name='addspending'),
    path('formoney',views.formoney,name='formoney'),



  path('register',views.register,name='register'),
  path('login',views.login,name='login'),
  path('logout',views.logout,name='home'),  

]