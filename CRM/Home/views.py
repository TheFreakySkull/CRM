from django.urls import reverse
from urllib.parse import urlencode

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User

from Home.forms import LoginForm, CreateUserForm


def show_home(request):
    error = request.GET.get('error')
    context = {'error': error}
    return render(request, 'home/index.html', context=context)

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home:main')
            else:
                return redirect_error('home:login', 'Такого пользователя не существует...')
        else:
            return redirect_error('home:login', 'Вы ввели данные неправильно...')
    else:
        if request.user.is_authenticated:
            logout(request)
            return redirect('home:main')

        error = request.GET.get('error')
        login_form = LoginForm()
        context = {'form': login_form, 'error': error}
        return render(request, 'home/login.html', context)

def create_user(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                email = form.cleaned_data['email']
                is_superuser = form.cleaned_data['is_superuser']
                users = User.objects.all()
                if users.filter(username=username) or users.filter(email=email):
                    return redirect_error('home:create_user', 'Такой пользователь уже существует!')

                if is_superuser:
                    User.objects.create_superuser(username=username, password=password, email=email)
                else:
                    User.objects.create_user(username=username, password=password, email=email)

                return redirect('main:crm')
            else:
                return redirect_error('home:create_user','Вы ввели данные неправильно...')
        error = request.GET.get('error')
        form = CreateUserForm()
        context = {'form': form, 'error': error}
        return render(request, 'home/create_user.html', context)
    else:
        return redirect_error('home:main', 'У вас не достаточно прав...')


def redirect_error(link, error):
    return redirect(
        f'{reverse(link)}?{urlencode(({'error': error}))}'
    )

"""Пароль не должен быть слишком похож на другую вашу личную информацию.
Ваш пароль должен содержать как минимум 8 символов.
Пароль не должен быть слишком простым и распространенным.
Пароль не может состоять только из цифр."""