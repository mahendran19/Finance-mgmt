from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import FormIncome,FormExpense
from .models import Income,Expense

import pickle
import pygal
from django.core.exceptions import ValidationError
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

        #form= FormRegister(request.POST or None)
        #if form.is_valid():
         #   form.save()
          #  form= FormIncome(request.POST or None)

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
    a=Income()
    incomes=Income.objects.filter(user_id=current_user.id)
    b=[a.salary for a in incomes]
    print(sum(b))
    
    if Income.objects.all():
            #Totalsalary=Income.objects.get(id=1).salary
        Totalsalary=sum(b)
        print(Totalsalary)
    else:
            Totalsalary=0
    
    expenses=Expense.objects.all()
    e=Expense()
    c=[e.expense for e in expenses]
    if Expense.objects.all():
        #Totalsalary=Income.objects.get(id=1).salary
        spend=sum(c)
    else:
        spend=0
    
    #a=Income()
    #print(a.salary)
    #b=[a.salary for i in incomes]
    
    
    #if Register.objects.filter(first_name) in e:
     #    incomes=Income.objects.filter(customer_firstname)
    
    #print(i)
    #if User.objects.filter(first_name=i).exists():   
   
    #print(incomes)
   
    
    Balance=Totalsalary-spend
    return render(request,'home1.html',{'totalsalary':Totalsalary,'balance':Balance,'spendingmoney':spend})

def income(request):
    
    #data = {'Task' : 'Hours per Day', 'Work' : 11, 'Eat' : 2, 'Commute' : 2, 'Watching TV' : 2, 'Sleeping' : 7}
	#print(data)
    food=20
    transport=30
    rent=40
    others=43

    return render(request,'income.html',{'f':food,'t':transport,'r':rent,'o':others})

def adding(request):
    
    salary=int(request.POST["salary"])
    
    if request.method=='POST':
        form= FormIncome(request.POST or None)
    
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()

            
        
    incomes=Income.objects.all()
    

    print(incomes)
    a=Income()
    b=[a.salary for a in incomes]
    Totalsalary=sum(b)
    print(Totalsalary)
    

    expenses=Expense.objects.all()
    e=Expense()
    c=[e.expense for e in expenses]
    spend=sum(c)
    print(spend)
    #context= {'form': form }
    
    Balance=Totalsalary-spend
    return render(request,'home2.html',{'Total':Totalsalary,'spendingmoney':spend,'balance':Balance})

def addincome(request):
    return render(request,'addincome.html')

def add2(request): 
    
        
    salary=int(request.POST["salary"])
    if request.method=='POST':
        form= FormIncome(request.POST or None)
    
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
    
    incomes=Income.objects.all()
    a=Income()
    b=[a.salary for a in incomes]
    Totalsalary=sum(b)
    

    expenses=Expense.objects.all()
    e=Expense()
    c=[e.expense for e in expenses]
        
    if Expense.objects.all():        
        spend=sum(c)
        
    else:
        spend=0

    
    print(Totalsalary)
  
    context= {'form': form }
    
    
    Balance=Totalsalary-spend
    return render(request,'home2.html',{'Total':Totalsalary,'spendingmoney':spend,'balance':Balance})

    
def addspending(request):
    return render(request,'addspending.html')

def formoney(request):
    incomes=Income.objects.all()
    a=Income()
    b=[a.salary for a in incomes]
    Totalsalary=sum(b)
    
    
    expense=int(request.POST["expense"])
    if request.method=='POST':
        form= FormExpense(request.POST or None)
    
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()

    
    
    
    expenses=Expense.objects.all()
    e=Expense()
    c=[e.expense for e in expenses]
    spend=sum(c)

    #if Expense.objects.get(id=1):
        #Totalsalary=Income.objects.get(id=1).salary
     #   spend=sum(c)
    #else:
     #   spend=0
    #if request.method=='POST':
     #   form= FormExpense(request.POST or None)
    
      #  if form.is_valid():
       #     forim.id
        #    form.save()
         #   form.id
        
    #expenses=Expense.objects.all()
    #c=[e.expense for a in expenses]
    #spend=sum(c)
    
    print(Totalsalary)
    print(spend)
  
    context= {'form': form }
    
    Balance=Totalsalary-spend
    
    return render(request,'home2.html',{'Total':Totalsalary,'spendingmoney':spend,'balance':Balance})


def spendmoney(request):
    
    return render(request,'money.html')


    















        
def login(request):

    
    if request.method !="POST":
        return render(request, 'login.html')
    if 'username' not in request.POST and not request.POST['username']:
        message.info(request, 'Username is required')
        return redirect('login')
    if 'password' not in request.POST and not request.POST['password']:
        message.info (request,'Password is not Match')
        return redirect('login')
    username=request.POST['username']
    password=request.POST['password']    
    user=auth.authenticate(username=username,password=password)
    
    db_list = []
    for key,value in request.POST.items():
        if key != "csrfmiddlewaretoken":
            db_list.append(value)
    file_name = 'hi.txt'
    outfile =  open(file_name,'wb')
    pickle.dump(db_list,outfile)
    outfile.close()
    

    if not user:
        messages.info(request,'invalid credentials')
        return redirect('login')
    auth.login(request,user)
    return redirect("/")

def logout(request):
    auth.logout(request)
    return redirect('/')
