from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect
# Create your views here.


def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
          print("form validated")
          print('Name:' , fm.cleaned_data['name'])
          print('roll:' , fm.cleaned_data['roll'])
          print('price:' ,fm.cleaned_data['price'])
          print('agree:' , fm.cleaned_data['agree'])
    else:    
        fm = StudentRegistration()

    return render(request , 'enroll/userregistration.html' , {'form' : fm})