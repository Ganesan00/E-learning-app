from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname','')
        lastname = request.POST.get('lastname','')
        username  = request.POST.get('username','')
        email = request.POST.get('email','')
        password1 = request.POST.get('password1','')
        password2 = request.POST.get('password2','')
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username is Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email is Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password1)
                user.save()
                print('user registered successfully')
                return redirect('login')
        else:
            print('password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, "register.html",{})
        

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,'successfully logged in')
            return redirect('/')
        else:
            messages.info(request, 'wrong username and password')
            return redirect('login')
    else:
        return render(request, "login.html",{})
    
def logout(request):
    auth.logout(request)
    return redirect('/')