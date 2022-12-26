from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username,password=password)
        print('user:',user,'\nusername:',username,'\npassword:',password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return render(request,'index.html')

def index(request):
    # context={'variable':'bwahahahahah'}
    # return render(request, 'index.html',context)
    # messages.success(request, 'Profile details updated.')
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def tool(request):
    if request.method=='POST':
        name=request.POST.get('name')
        foto=request.POST.get('foto')
        email=request.POST.get('email')
        service=request.POST.get('service')
        more_service=request.POST.get('more_service')
        contact=Contact(name=name, foto=foto, email=email, service=service, more_service=more_service,
        date=datetime.now())
        contact.save()
        messages.success(request, 'Banda Khtm Smjo 💀')


    return render(request, 'tool.html')
def gallery(request):
    return render(request, 'gallery.html')
