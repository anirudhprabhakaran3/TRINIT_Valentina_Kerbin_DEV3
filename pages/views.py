from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from pages.forms import SignUpForm
from pages.models import Profile


# Create your views here.
def home(request):
    return render(request, 'pages/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            new_profile = Profile()
            new_profile.user = user
            new_profile.phone_number = form.cleaned_data.get('phone_number')
            new_profile.location = form.cleaned_data.get('location')
            new_profile.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('pages_profile')
    else:
        form = SignUpForm()
    args = {
        'form': form,
    }
    return render(request, 'pages/signup_form.html', args)


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    args = {
        'user': user,
    }
    return render(request, 'pages/profile.html', args)
