from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import FormContactForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ContactForm
from .serializers import ContactFormSerializer
import pickle

# Create your views here.

Totalsalary=0

def home(request):
    return render(request,'home1.html')
    

def add(request):   
    global Totalsalary
    salary=int(request.POST["salary"])
    others=int(request.POST["others"])
          
    Totalsalary=salary+others
   

    form= FormContactForm(request.POST or None)
          
    if form.is_valid():
        form.save()
    
    return render(request, 'home.html',{'totalincome':Totalsalary,'form':form})
    return redirect('/')

def spendmoney(request):
    
    return render(request,'money.html')



def formoney(request):
    global food
    global rent
    global transport
    global others
    
    global totalspend
    global BalanceRs
    global totalspend    


    food=int(request.POST['food'])
    rent=int(request.POST['r'])
    transport=int(request.POST['t'] )
    others=int(request.POST['o'])
    
    
    
    totalspend=food+rent+transport+others  
    BalanceRs=Totalsalary-totalspend  

    
    
    f=(food/Totalsalary)*100
    r=(rent/Totalsalary)*100
    t=(transport/Totalsalary)*100
    o=(others/Totalsalary)*100
    form= FormContactForm(request.POST or None)
    newfile = open("db_storage",'rb')
    
    return render(request,'home2.html',{'totalincome':Totalsalary,'spendingmoney':totalspend,'balance':BalanceRs,'f':f,'r':r,'t':t,'o':o})




def income(request):            
    return render(request, 'income.html')
    
  
def addincome(request):
    return render(request,'addincome.html')




def addspending(request):
    return render(request,'addspending.html')
    return redirect('formoney')



    
    
def formoney1(request):
   
    
    formoney(request)
    plusincome=int(request.POST["plusincome"])
    nexttotalsalary=Totalsalary+plusincome
    
             
    return render(request,'home7.html',{'totalincome':nexttotalsalary,'spendingmoney':totalspend,'balance':BalanceRs,'f':f,'r':r,'t':t,'o':o})
    
        

def morespending(request):
    global f
    global r
    global t
    global o
    
    f=(food/Totalsalary)*100
    r=(rent/Totalsalary)*100
    t=(transport/Totalsalary)*100
    o=(others/Totalsalary)*100
    return render(request,'morespending.html',{'f':f,'r':r,'t':t,'o':o})

def nextaddmoney(request):
    f,r,t,o=morespending(request)
    plusincome=int(request.POST["plusincome"])
    nexttotalsalary=Totalsalary+plusincome
    return render(request,'home7.html',{'totalincome':nexttotalsalary,'spendingmoney':totalspend,'balance':BalanceRs,'f':f,'r':r,'t':t,'o':o})
    
    
    

def totalincomes(request):
    return render(request, 'result.html',{'totalincome':Totalsalary})



def login(request):
    if request.method=="POST":
        username=request.POST['username']

        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")

        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


def register(request):
    if request.method=='POST':
        global first_name
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        
        


        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken')
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

    
def logout(request):
    auth.logout(request)
    return redirect('/')


@api_view(['GET'])
def apiOverview(request):
    api_urls={

        'List':'/task-list',
        'Detail View':'/task-details/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk/',
    }
    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    tasks=Task.objects.all()
    serializer=ContactForm(tasks,many=True)
    return Response(serializer.data)



def serial(request):
    form= FormContact1(request.POST or None)
    if form.is_valid():
        form.save()
    context= {'form': form }
    return render(request, 'income.html', context)
