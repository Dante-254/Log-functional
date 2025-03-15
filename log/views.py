
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.http import HttpResponse



# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    User = get_user_model()
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in use')
                return redirect('register')
                
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already in use')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save
                messages.success(request, 'Account created successfully')
                user = auth.authenticate(username=username, password=password)
                login_user(request)
                return redirect('/')
        else:
            messages.info(request, 'password not same')
            return redirect('register')
    
    return render(request, 'register.html')

def login_user(request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User = auth.authenticate(username=username, password=password)

        if User is not None:
            auth.login(request, User)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
     else:
      return render(request, 'login.html')
     
def logout_user(request):
    auth.logout(request)
    return redirect('/')

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})

def counter(request):
    per_blog = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    return render(request, 'counter.html', {'per_blog' : per_blog})

def tables(request):
    users = User.objects.all()
    return render(request, 'tables.html', {'users': users})