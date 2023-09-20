from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import update_session_auth_hash

from apps.users.forms import LoginForm, SignUpForm, UpdateUserName, UpdatePassword
from apps.revise_minder.models import Study, Subject

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

    return redirect("index")

def my_account(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    user = request.user
    user_name = user.username

    if request.method == "POST":
        form = UpdateUserName(request.POST)

        if form.is_valid():
            user_name = form["user_name"].value()

            if User.objects.filter(username=user_name).exists():
                return redirect("my_account")

            if user_name != "" or user_name:
                user.username = user_name
                user.save()

    return render(request, 'users/my_account.html', {"user_name": user_name})

def update_password(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "users/update_password.html")

def delete_account(request):
    user = request.user
    studies = Study.objects.filter(user=user)
    subjects = Subject.objects.filter(user=user)

    studies.delete()
    subjects.delete()
    user.delete()
    return redirect('index')