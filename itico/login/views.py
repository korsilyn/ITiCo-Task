from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import add_message, SUCCESS, ERROR
from .forms import LoginForm

def index(request):
    return render(request, 'index.html', get_base_context(request))

def login_page(request):
    if request.method == 'POST':
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username = loginform.data['username']
            password = loginform.data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                add_message(request, SUCCESS, 'Авторизация успешна')
                return redirect('index')
            add_message(request, ERROR, 'Неправильный логин или пароль')
            return redirect('login')
        add_message(request, ERROR, 'Некорректные данные в форме авторизации')
        return redirect('login')

    context = get_base_context(request, {
        'form': LoginForm()
    })

    return render(request, 'login.html', context)

def register_page(request):
    if request.method == 'POST':
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            regform.save()
            username = regform.data['username']
            password = regform.data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                add_message(request, SUCCESS, 'Регистрация успешна')
                return redirect('index')
            add_message(request, ERROR, 'Ошибка регистрации')
            return redirect('register')
        add_message(request, ERROR, 'Некорректные данные')
        return redirect('register')

    context = get_base_context(request, {
        'form': UserCreationForm()
    })
    return render(request, 'register.html', context)

@login_required
def logout_page(request):
    logout(request)
    add_message(request, SUCCESS, "Вы успешно вышли из аккаунта")
    return redirect('index')

def get_base_context(request, update=None):
    context = {
        'request': request,
        'user': request.user,
    }

    if isinstance(update, dict):
        context.update(update)

    return context
