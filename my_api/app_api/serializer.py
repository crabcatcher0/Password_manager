from rest_framework import serializers
from .models import UserData

class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserData
        fields = ('site_name', 'password', 'note') 