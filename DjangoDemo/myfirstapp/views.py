import profile
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

def home(request):
    return render(request,'home.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserprofileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserprofileInfoForm()
    return render(request,'registeration.html',{'user_form':user_form,
                                                'profile_form':profile_form,
                                                'registered':registered})
