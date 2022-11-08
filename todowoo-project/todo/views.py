from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todo


def home(request):
    return render(request, 'todo/home.html')


def sign_up_user(request):
    if request.method == 'GET':
        return render(request, 'todo/sign_up_user.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('current_todos')
            except IntegrityError:
                return render(request, 'todo/sign_up_user.html',
                              {'form': UserCreationForm(), 'error': 'Имя пользователя уже используется'})
        else:
            return render(request, 'todo/sign_up_user.html',
                          {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


def create_todo(request):
    if request.method == 'GET':
        return render(request, 'todo/create_todo.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect('current_todos')
        except ValueError:
            return render(request, 'todo/create_todo.html',
                          {'form': TodoForm(), 'error': 'Длина введенного текста превышает разрешенное значение'})


def current_todos(request):
    todos = Todo.objects.all()
    return render(request, 'todo/current_todos.html', {'todos': todos})


def login_user(request):
    if request.method == 'GET':
        return render(request, 'todo/login_user.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request=request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'todo/login_user.html',
                          {'form': AuthenticationForm(), 'error': 'Пользователь не найден'})
        else:
            login(request, user)
            return redirect('current_todos')


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
