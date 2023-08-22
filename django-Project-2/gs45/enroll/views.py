from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def show_form_data(request):
    fm = StudentRegistration()
    return render(request , 'enroll/userregistration.html' , {'form' : fm})
