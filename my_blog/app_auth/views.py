from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *

# Create your views here.
def login_blog(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user = authenticate(username=username,password=pwd)
            if user is not None:
                login(request,user)
              
                return redirect('home')
            else:
                messages.error(request,"Authentification échouée")
                return render(request,'login.html',{'form':form})
        else:
             for field in form.errors:
                 
              form[field].field.widget.attrs['class'] += 'is-invalid'

             return render(request,'login.html',{'form':form})
    else :

        form = loginForm()
        return render(request,'login.html',{'form':form})
    

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user = User.objects.create_user(username=username, password=pwd)
            if user is not None:
                return redirect("login-blog")
            else:
                messages.error(request, 'Création compte échouée')
                return render(request, 'register.html', {'form': form})
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    

def logout_blog(request):
    logout(request)
    return redirect('login-blog')


       
