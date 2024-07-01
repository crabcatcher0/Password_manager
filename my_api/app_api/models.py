from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserData(models.Model):
    site_name = models.CharField(max_length=225, null=False)
    password = models.CharField(max_length=225, null=False)
    note = models.CharField(max_length=225, null=True, default='-No notes were created.')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.site_name
    

class Mysite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    site_name = models.CharField(max_length=225, null=False)
    password = models.CharField(max_length=225, null=False)
    note = models.CharField(max_length=225, null=True, default='-No notes were created.')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.site_name
    