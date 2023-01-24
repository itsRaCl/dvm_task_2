from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.socialaccount.forms import SignupForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    QuizMaster = forms.BooleanField(required=False)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "QuizMaster", "email", "password1", "password2")


class CustomUserGoogleCreationForm(SignupForm):
    QuizMaster = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, request):
        # Set the user's type from the form reponse
        user = super(CustomUserGoogleCreationForm, self).save(request)
        user.QuizMaster = self.cleaned_data["QuizMaster"]
        # Save the user's type to their database record
        user.save()


class CustomUserChangeForm(UserChangeForm):
    QuizMaster = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ("username", "QuizMaster")
