# Create your views here.
from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from .serializer import DataSerializer
from django.contrib import messages
from .models import UserData
from .forms import RegisterForm
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
        else:
            form = RegisterForm()
            form.errors
            
    context = {
        'form':form
    }
    return render(request, 'register.html', context)
