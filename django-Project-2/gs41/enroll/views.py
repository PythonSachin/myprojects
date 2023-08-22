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
        #   st = Student(name = nm , email = em , password = pd) creating new student in database
        #   st = Student(id = 1 , name = nm , email = em , password = pd) updating student with id = 1
            # st.save()

          st = Student(id = 1)
          st.delete();
    else:    
        fm = StudentRegistration()

    return render(request , 'enroll/userregistration.html' , {'form' : fm})