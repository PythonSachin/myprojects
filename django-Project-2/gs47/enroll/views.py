from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages
# Create your views here.

def regi(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.info(request , "You are now a registered user")
            print(messages.get_level(request))
            messages.set_level(request , messages.DEBUG)
            messages.debug(request , "This is Debug")
            print(messages.get_level(request))
    else:
        fm = StudentRegistration()

    return render(request , 'enroll/userregistration.html' , {'form' : fm})            
