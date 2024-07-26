# Create your views here.
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, logout
from .serializer import DataSerializer
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import UserData, Mysite
from .forms import RegisterForm, LoginForm, MysiteForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from module1 import func


def home(request):
    return render(request, 'home.html')


def generate_pass(request):
    if request.method == 'POST':
        data = func.create_pass(15)
        context = {
            'data':data
        }
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')



@api_view(['GET', 'POST'])
def my_data(request):
    if request.method == 'GET': 
        querryset = UserData.objects.all()
        serializer = DataSerializer(querryset, many=True)
        serialized_data = serializer.data

        return Response(serialized_data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        add_serializer = DataSerializer(data = request.data)
        if add_serializer.is_valid():
            data1 = add_serializer.save()

            return Response(data1, status=status.HTTP_201_CREATED)



def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = RegisterForm()
            messages.error(request, 'Error: Please check all fileds.')
            
    context = {
        'form':form
    }
    return render(request, 'register.html', context)



def user_login(request):
    if request.user.is_authenticated:
        return redirect('account')  
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('account', id=user.id) 
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
       


def user_logout(request):
    logout(request)
    return redirect('home')



def account(request, id):
    user_data = get_object_or_404(User, pk=id)
    data = Mysite.objects.filter(user_id = id)
    context = {
        'user_data':user_data,
        'data':data
    }
    return render(request, "account.html", context)


def add_data(request, id):
    if request.method == 'POST':
        form = MysiteForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=id)
            
            mysite_instance = form.save(commit=False)
            mysite_instance.user_id = id
            mysite_instance.save()
            
            messages.success(request, 'Data added successfully.')
            return redirect('account', id=id)
        else:
            messages.error(request, 'Error: Please check all fields.')
    else:
        form = MysiteForm()
    
    context = {
        'form': form
    }
    return render(request, "account.html", context)

