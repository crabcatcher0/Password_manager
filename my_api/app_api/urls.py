from django.urls import path
from .views import my_data

urlpatterns = [
    path('my_data/', my_data, name="my_data")
]