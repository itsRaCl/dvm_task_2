from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    QuizMaster = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ("username", "QuizMaster", "password1", "password2")


class CustomUserChangeForm(UserChangeForm):
    QuizMaster = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ("username", "QuizMaster")
