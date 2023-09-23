from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth import update_session_auth_hash, authenticate

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
                messages.error(request, "Nome de usuário ou senha incorretos.")
                return redirect("login")

    return render(request, 'users/login.html', {"form": form})

def signup(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            if form["password_1"].value() != form["password_2"].value():
                messages.error(request, "As duas senhas precisam ser iguais.")
                return redirect("signup")
            
            name = form["sign_up_name"].value()
            password = form["password_1"].value()

            if User.objects.filter(username=name).exists():
                messages.error(request, "Nome de usuário não disponível.")
                return redirect("signup")
            
            user = User.objects.create_user(
                username=name,
                password=password
            )
            user.save()

            messages.success(request, "Cadastro feito com sucesso.")
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
                messages.error(request, "Nome de usuário não disponível.")
                return redirect("my_account")

            if user_name != "" or user_name:
                user.username = user_name
                messages.success(request, "Nome de usuário alterado com sucesso.")
                user.save()

    return render(request, 'users/my_account.html', {"user_name": user_name})

def update_password(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    form = UpdatePassword()

    if request.method == 'POST':
        form = UpdatePassword(request.POST)

        if form.is_valid():
            user = authenticate(username=request.user.username, password=form.cleaned_data['current_password'])
            
            if user is not None:
                user.set_password(form.cleaned_data['new_password1'])
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Senha alterada com sucesso.")
                return redirect('my_account')
            else:
                messages.error(request, "Senha atual incorreta.")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Erro no campo {field}: {error}")

    return render(request, "users/update_password.html", {"form": form})

def delete_account(request):
    user = request.user
    studies = Study.objects.filter(user=user)
    subjects = Subject.objects.filter(user=user)

    studies.delete()
    subjects.delete()
    user.delete()
    messages.success(request, "Conta excluida com sucesso.")
    return redirect('index')