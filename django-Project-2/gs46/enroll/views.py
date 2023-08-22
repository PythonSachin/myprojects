from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages
# Create your views here.

def regi(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request , messages.SUCCESS , 'Your registration was succesfull') # or
            messages.info(request , "You are now a registered user")
    else:
        fm = StudentRegistration()

    return render(request , 'enroll/userregistration.html' , {'form' : fm})            
