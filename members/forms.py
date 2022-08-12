from datetime import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone

class UserRegistrationForm(UserCreationForm):
    firstname = forms.CharField(max_length=101)
    lastname = forms.CharField(max_length=101)
    email = forms.EmailField()
    username = forms.CharField(max_length=255)
    age = forms.CharField(max_length=255)
    image= forms.ImageField()
    gender= forms.CharField(max_length=255)
    #reg_date = forms.DateTimeField()

    class Meta:
        model = User
        fields = ['username', 'firstname', 'lastname', 'email', 'password1', 'password2',
        'age','gender']


