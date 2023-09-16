#-----------CREATE OPERATION------------
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import body
from django.contrib.auth.models import auth
def create(request):
    if request.method=='POST':
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        obj=body.objects.create(name=name,mobile=mobile,password=password)
        if password==confirm_password:
            obj.save()
            return redirect('login')
        else:
            return HttpResponse("invalid crendiations")
    else:    
        return render(request,'create.html')
    

#-----------------LOGIN OPERTION-------------


def login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        data=body.objects.get(name=name,password=password)
        if(data is not None):
         return redirect('home')
    else:
        return render(request,'login.html')    
    


#------------WEBSITE PAGE---------------


def home(request):
    return render(request,'home.html')


#----------LOGOUT OPERATION------------

def logout(request):
    auth.logout(request)
    return redirect('login')