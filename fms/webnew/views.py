from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import FormIncome2,FormExpense2
from .models import Income2,Expense2

import pickle
import pygal
from django.core.exceptions import ValidationError
from django. contrib. auth import authenticate
import pygal

# Create your views here.
def register(request):
    global first_name
    
    if request.method=='POST':        
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        email=request.POST["email"]

        min_length=8
        if (len(password1)<min_length):
            messages.info(request,"The password must be at least %d characters long." %min_length)
            return redirect('register')
        if (password1.isalpha()==True):
            messages.info(request,"Password Must contains Atleaset one Numeric")
            return redirect('register')
        if(password1.isnumeric()==True):
            messages.info(request,"Password Must contains Atleaset one Alphabet")
            return redirect('register')
        if password1==password2:
            
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already taken,Try with new one')
                
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken, Try with new one')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')                
                return redirect('login')     
            
        else:
            
            messages.info(request,'password not matching')
            
            return redirect('register')
        return redirect('login')
    else:
            return render(request,'register.html')




def home(request):
    current_user=request.user
    
    print(current_user.id)
    a=Income2()
    incomes=Income2.objects.filter(user_id=current_user.id)
    b=[a.salary for a in incomes]
    print(sum(b))
   
    
    if Income2.objects.all():
            #Totalsalary=Income.objects.get(id=2).salary
        Totalsalary=sum(b)
        print(Totalsalary)
    else:
            Totalsalary=0
    
    expenses=Expense2.objects.filter(user_id=current_user.id)
    e=Expense2()
    f=[e.Food for e in expenses]
    r=[e.Rent for e in expenses]
    t=[e.Transport for e in expenses]
    o=[e.Others for e in expenses]
    if Expense2.objects.filter(user_id=current_user.id):
        #Totalsalary=Income.objects.get(id=2).salary
        spend=sum(f)+sum(r)+sum(t)+sum(o)
    else:
        spend=0

    Balance=Totalsalary-spend
    return render(request,'home8.html',{'f':sum(f),'r':sum(r),'t':sum(t),'o':sum(o),'totalsalary':Totalsalary,'balance':Balance,'Spendingmoney':spend})

def income(request):

    return render(request,'income.html')

def adding(request):
    
    current_user=request.user
    
    
    if request.method=='POST':
        form= FormIncome2(request.POST or None)
    
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()

            
        
    incomes=Income2.objects.filter(user_id=current_user.id)
    

    print(incomes)
    a=Income2()
    b=[a.salary for a in incomes]
    Totalsalary=sum(b)
    print(Totalsalary)
    

    expenses=Expense2.objects.filter(user_id=current_user.id)
    e=Expense2()
    f=[e.Food for e in expenses]
    r=[e.Rent for e in expenses]
    t=[e.Transport for e in expenses]
    o=[e.Others for e in expenses]
    spend=sum(f)+sum(r)+sum(t)+sum(o)
    print(spend)
    #context= {'form': form }
    
    Balance=Totalsalary-spend
    return render(request,'home2.html',{'f':sum(f),'r':sum(r),'t':sum(t),'o':sum(o),'totalsalary':Totalsalary,'spendingmoney':spend,'balance':Balance})

def addincome(request):
    return render(request,'addincome.html')

def add2(request): 
    current_user=request.user
        
    salary=int(request.POST["salary"])
    if request.method=='POST':
        form= FormIncome2(request.POST or None)
    
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
    
    incomes=Income2.objects.filter(user_id=current_user.id)
    a=Income2()
    b=[a.salary for a in incomes]
    Totalsalary=sum(b)
    

    expenses=Expense2.objects.filter(user_id=current_user.id)
    e=Expense2()
    
    f=[e.Food for e in expenses]
    r=[e.Rent for e in expenses]
    t=[e.Transport for e in expenses]
    o=[e.Others for e in expenses]
    if Expense2.objects.filter(user_id=current_user.id):  
        spend=sum(f)+sum(r)+sum(t)+sum(o)
        
    else:
        spend=0

    
    print(Totalsalary)
    context= {'form': form }
    
    Balance=Totalsalary-spend
    return render(request,'home2.html',{'Total':Totalsalary,'spendingmoney':spend,'balance':Balance})

    
def addspending(request):

    return render(request,'adds.html')

def formoney(request):
    current_user=request.user
    incomes=Income2.objects.filter(user_id=current_user.id)
    a=Income2()
    b=[a.salary for a in incomes]
    Totalsalary=sum(b)
    
    
    
    if request.method=='POST':
        form= FormExpense2(request.POST or None)
    
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()

    
    
    
    expenses=Expense2.objects.filter(user_id=current_user.id)
    e=Expense2()
    f=[e.Food for e in expenses]
    r=[e.Rent for e in expenses]
    t=[e.Transport for e in expenses]
    o=[e.Others for e in expenses]
    spend=sum(f)+sum(r)+sum(t)+sum(o)

    print(Totalsalary)
    print(spend)
  
    
    
    Balance=Totalsalary-spend
    
    return render(request,'formoney.html',{'f':sum(f),'r':sum(r),'t':sum(t),'o':sum(o),'totalsalary':Totalsalary,'spendingmoney':spend,'balance':Balance})


def spendmoney(request):
    
    return render(request,'money.html')



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
        

def logout(request):
    auth.logout(request)
    return redirect('/')
