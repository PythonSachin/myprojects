from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages

# Create your views here.

def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save();
            messages.success(request , "User created successfully")

    else:
        fm = SignUpForm()
    return render(request , 'enroll/signup.html' , {'form' : fm})