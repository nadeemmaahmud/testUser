from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth
from . models import dataDB

def home(request):
    if request.method == 'POST':
        info = dataDB()
        info.name = request.POST['name']
        info.data = request.POST['data']
        if info.name == '' and info.data == '':
            messages.info(request, 'Something went wrong!')
            return redirect('/')
        else:
            info.user = request.user
            info.save()
            messages.info(request, "Saves Successfully!")
            return redirect('/')
        
    db = dataDB.objects.all()
    return render(request, 'index.html', {'db':db})
    
def register(request):
    if request.method == 'POST': 
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        username = request.POST['userName']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, "Registration Successful!")
                return redirect('login')
        else:
            messages.info(request, "Password not matched!")
            return redirect('register')
        
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Wrong Username or Password!")
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')
    