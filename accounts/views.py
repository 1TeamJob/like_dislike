from django.shortcuts import render, redirect
from .models import Profile
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from django.urls import reverse



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password=password)
            login(request, user)
            return redirect(reverse('/accounts/profile/'))
    
    
    else:
        form = SignupForm
    
    context = {'form': form}
    return render(request, 'registration/signup.html', context)


def profile(request):
    profile = Profile.objects.all()
    
    context = {'profile': profile}
    return render(request, 'accounts/profile.html', context)
