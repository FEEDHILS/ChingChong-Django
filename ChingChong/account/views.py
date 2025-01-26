from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import User
from django.contrib.auth.forms import *
from django.contrib.auth import login, logout, get_user_model
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

# AUTHENTIFICATION AND REGISTRATION...

def login_user(req):
    AuthForm = AuthenticationForm()
    if req.method == 'POST':
        AuthForm = AuthenticationForm(data=req.POST, request=req)
        if AuthForm.is_valid():
            user = AuthForm.get_user()
            login(req, user)
            return redirect('index')
        
    return render(req, 'account/authorization.html', {'form': AuthForm})

def logout_user(req):
    if req.user.is_authenticated:
        logout(req)
    
    return redirect('index')

def register(req):
    RegisterForm = UserRegisterForm()
    if req.method == 'POST':
        genderM = req.POST.get('genderM')
        genderF = req.POST.get('genderF')
        gender = 'D'
        if genderM == 'on':
            gender = 'M'
        elif genderF == 'on':
            gender = 'F'

        data = req.POST.copy()
        data['gender'] = gender  

        RegisterForm = UserRegisterForm(data=data)
        if RegisterForm.is_valid():
            user = RegisterForm.save()
            login(req, user)
            return redirect('index')
        

    return render(req, 'account/registration.html', {'form': RegisterForm})


# PASSWORD RESTORATION STUFF...

# Страничка с формой ввода Email, для восст. пароля.
def forgot(req):
    if req.method == "GET":
        EmailForm = PasswordResetForm()
    else:
        EmailForm = PasswordResetForm(req.POST)
        if EmailForm.is_valid():
            EmailForm.save(request=req)
            return redirect('password_reset/confirmed')

    return render(req, "account/resetPassword.html", { "form": EmailForm })

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
                # print("Password has Changed")
                return redirect('index')

        return render(req, "account/resetNewPassword.html", { "form": PassForm }) 
    else:
        return redirect('index')


# PROFILE STUFF...

def profile(req, name=None):
    print(name)
    if name is None:
        user = req.user
    else:
        user = get_object_or_404(get_user_model(), username=name)
    
    # print(user.gender)
    return render(req, "account/personalSpace.html", {'current': user})