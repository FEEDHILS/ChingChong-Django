from django.shortcuts import render, redirect
from .forms import *
from .models import User
from django.contrib.auth.forms import *
from django.contrib.auth import login, logout, get_user_model
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

def login_user(req):
    AuthForm = AuthenticationForm()
    if req.method == 'POST':
        AuthForm = AuthenticationForm(data=req.POST, request=req)
        if AuthForm.is_valid():
            user = AuthForm.get_user()
            login(req, user)
            return redirect('index')
        
    return render(req, 'login.html', {'form': AuthForm})


def register(req):
    RegisterForm = UserRegisterForm()
    if req.method == 'POST':
        RegisterForm = UserRegisterForm(data=req.POST)
        if RegisterForm.is_valid():
            user = RegisterForm.save()
            login(req, user)
            return redirect('index')
        

    return render(req, 'registration.html', {'form': RegisterForm})

def logout_user(req):
    if req.user.is_authenticated:
        logout(req)
    
    return redirect('index')

# Страничка с формой ввода Email, для восст. пароля.
def forgot(req):
    if req.method == "GET":
        EmailForm = PasswordResetForm()
    else:
        EmailForm = PasswordResetForm(req.POST)
        if EmailForm.is_valid():
            EmailForm.save(request=req)
            return redirect('password_reset/confirmed')

    return render(req, "password_reset.html", { "form": EmailForm })

def reset_confirmed(req, uidb64, token):
    id = urlsafe_base64_decode(uidb64).decode()
    user = get_user_model().objects.get(pk=id)

    if PasswordResetTokenGenerator().check_token(user, token):
        if req.method == "GET":
            PassForm = SetPasswordForm(user=user)
        else:
            PassForm = SetPasswordForm(user, req.POST)
            if PassForm.is_valid():
                PassForm.save()
                print("Password has Changed")
                return redirect('index')

        return render(req, "password_reset.html", { "form": PassForm }) 
    else:
        return redirect('index')

