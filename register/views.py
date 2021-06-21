from django.shortcuts import render
from .forms import LoginForm,SignUpForm
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User, Group
from order.models import *

# Create your views here

def signup_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save(is_seller=False)
            username = form.cleaned_data.get('username')
            print(username)
            raw_password = form.cleaned_data.get('password1')
            print(raw_password)

            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'login/admin.html', {'form': form, 'is_seller': False})

def signup_seller(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save(is_seller=True)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.is_staff = True
            login(request, user)
            return redirect('/admin')
    else:
        form = SignUpForm()
    return render(request, 'login/admin.html', {'form': form, 'is_seller': True})


def log_out(request):
    logout(request)
    return redirect("../../")