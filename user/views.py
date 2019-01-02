from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def index(request):
    return render(request, 'user/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # this message will show us success of create our user
            messages.success(request, f'Account created for {username}!')
            return redirect('home')

    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})
