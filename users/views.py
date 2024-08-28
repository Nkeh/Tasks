from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import LoginForm, SignUpForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.views import LogoutView
# Create your views here.

def userLogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST, )
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome {username}')
                return redirect('home')
            else:
                messages.error(request, 'Invalid Credentials')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account successfully created for {username}!')
            return redirect('home')
    else:
        form = SignUpForm()
        messages.error(request, 'Unable to create user. try again')

    return render(request, 'users/register.html', {'form': form})


def userLogout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('home')
    return render(request, 'users/logout.html')
    

