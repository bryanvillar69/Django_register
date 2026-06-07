from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

#superuser
# admin, pass0000


def home(request):

    return render(request, 'home.html', {})

def register_user(request):
    return render(request, 'register.html', {})

def members(request):
    return render(request, 'members.html', {})

def login_user(request):
    # TO CHECK TO SEE IF LOGGING IN
    if request.method == 'POST':
        username =request.POST['username']
        password = request.POST['password']

        # AUTHENTICATE
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in, Please try again.")
            return redirect('login')

    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('login')
