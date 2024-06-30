# Create your views here.
from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from .serializer import DataSerializer
from .models import UserData
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


def home(request):
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