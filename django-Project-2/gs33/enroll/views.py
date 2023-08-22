from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showformdata(request):
    print("---------------------")
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        print(fm)
        print("Ye request POST se aaya h")
    else:    
        print("Ye request GET se aaya h")
        fm = StudentRegistration()

    return render(request , 'enroll/userregistration.html' , {'form' : fm})