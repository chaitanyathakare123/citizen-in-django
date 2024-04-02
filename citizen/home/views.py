from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from .forms import register



# Create your views here.
def index(request):
    context={
        
    }
    return render(request,'index.html',context)
    #return HttpResponse("this is homepage")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is services page")

def track(request):
    return render(request,'track.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'your message as been send!')
    return render(request,'contact.html')
    #return HttpResponse("this is contact page")

def login(request):
  return render(request,'login.html')

def register(request):
  return render(request,'register.html')

def logout(request):
    return render(request,'logout.html')

def live(request):
    return render(request,'live.html')    


def flags(request):
    return render(request,'flags.html')
