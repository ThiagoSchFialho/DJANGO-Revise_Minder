from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from apps.users.forms import LoginForm, SignUpForm

def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            name = form["login_name"].value()
            password = form["password"].value()

            user = auth.authenticate(
                request,
                username=name,
                password=password
            )

            if user is not None:
                auth.login(request, user)
                return redirect("revisions_home")
            else:
                return redirect("login")

    return render(request, 'users/login.html', {"form": form})

def signup(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            if form["password_1"].value() != form["password_2"].value():
                return redirect("signup")
            
            name = form["sign_up_name"].value()
            password = form["password_1"].value()

            if User.objects.filter(username=name).exists():
                return redirect("signup")
            
            user = User.objects.create_user(
                username=name,
                password=password
            )
            user.save()

            return redirect("login")

    return render(request, 'users/signup.html', {"form": form});

def logout(request):
    auth.logout(request)

    return redirect("login")