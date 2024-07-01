from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Mysite

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class MysiteForm(forms.ModelForm):
    class Meta:
        model = Mysite
        fields =  ['site_name', 'password', 'note']