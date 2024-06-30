from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('my_data/', my_data, name="my_data")
]