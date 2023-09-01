from django.shortcuts import render
from apps.users.forms import LoginForm, SignUpForm

def login(request):
    formulario = LoginForm()
    return render(request, 'users/login.html', {"form": formulario})

def signup(request):
    formulario = SignUpForm()
    return render(request, 'users/signup.html', {"form": formulario});