from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def index(request):
    return render(request, 'user/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # this message will show us success of create our user
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


# user must be logged in to view this page
@login_required
def profile(request):
    return render(request, 'user/profile.html')