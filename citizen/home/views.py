
from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from home.models import Contact,Complaint
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

def index(request):
      return render(request,'index.html')
    #return HttpResponse("this is about page")

@login_required
def services(request):
    user = request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        title = request.POST.get('title')
        category = request.POST.get('category')
        description = request.POST.get('description')
        urgency = request.POST.get('urgency')
        attachments = request.FILES.get('attachments')
        latitude=request.POST.get('latitude')
        longitude=request.POST.get('longitude')

        complaint = Complaint.objects.create(name=name, title=title, category=category, description=description, urgency=urgency, attachments=attachments,latitude=latitude,longitude=longitude,user=user)
        complaint.user=user
        complaint.save()

        messages.success(request, 'Complaint submitted successfully!')
        return redirect('flags')

    return render(request, 'services.html')
    #return HttpResponse("this is services page")

def track(request):
    return render(request,'track.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        title=request.POST.get('title')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,title=title,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'your message as been send!')
    return render(request,'contact.html')
    #return HttpResponse("this is contact page")
def login_user(request):
   if request.method=="POST":
         username=request.POST['username']
         password=request.POST['password']
         user=authenticate(request,username=username,password=password)
         if user is not None:
             login(request,user)
             messages.success(request,'You are now logged in!')
             return redirect('index')
         else:
             messages.success(request, 'Username or Password is incorrect')
             return redirect('login')
   else:
        return render(request, 'login.html')
   
def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            
            login(request,user)
            messages.success(request, "You Have Register successfully")
            return redirect('index')
        else:
              messages.error(request, 'Whoops! There was a problem try again!!')
    return render(request, "register.html", {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request,('Logged Out Successfully!'))
    return redirect('index')

@login_required
def flags(request):
   
    complaints=Complaint.objects.filter(user=request.user)
    return render(request,'flags.html',{'complaints':complaints})

def live(request):
    return render(request,'live.html')    
