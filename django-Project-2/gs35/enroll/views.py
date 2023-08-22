from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect
# Create your views here.


def thankYou(request):
    return render(request , 'enroll/success.html');


def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
          name = fm.cleaned_data['name']
          email = fm.cleaned_data['email']
          password = fm.cleaned_data['password']
        #   return render(request , 'enroll/success.html' , {'nm' : name})
          return HttpResponseRedirect('/regi/success/')
    else:    
        fm = StudentRegistration()

    return render(request , 'enroll/userregistration.html' , {'form' : fm})