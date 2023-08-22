from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect
from .models import Student
# Create your views here.


def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
          print("form validated")
          nm = fm.cleaned_data['name']
          em = fm.cleaned_data['email']
          pd = fm.cleaned_data['password']
          print(nm);
          print(em);
          print(pd);
    else:    
        fm = StudentRegistration()

    return render(request , 'enroll/userregistration.html' , {'form' : fm})