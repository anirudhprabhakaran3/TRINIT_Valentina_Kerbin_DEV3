from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    phone_number = forms.IntegerField(help_text="Enter your mobile number")
    location = forms.CharField(max_length=200, help_text="Enter the name of the city/village you live in.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
