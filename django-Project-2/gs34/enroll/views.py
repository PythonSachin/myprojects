from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showformdata(request):
    print("---------------------")
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
          print(fm.cleaned_data['name'])
          print(fm.cleaned_data['email'])
    else:    
        print("Ye request GET se aaya h")
        fm = StudentRegistration()

    return render(request , 'enroll/userregistration.html' , {'form' : fm})