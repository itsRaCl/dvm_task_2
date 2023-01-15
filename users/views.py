from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.http import HttpResponse
from .models import User

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect("profile", request.user.username)
    else:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get("username")
                return redirect("login")
        else:
            form = CustomUserCreationForm()
        return render(request, "users/register.html", {"form": form})


def profile(request, username):
    user = User.objects.get(username=username)
    context = {"user": user}
    return render(request, "users/profile.html", context=context)
