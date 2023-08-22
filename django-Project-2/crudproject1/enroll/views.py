from django.shortcuts import render
from .forms import StudentRegistration
from .models import Student
from django.http import HttpResponseRedirect
# Create your views here.


# This function will add new item and show all items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST);
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            eml = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password']
            reg = Student(name = nm , email = eml , password = pwd) 
            reg.save()
            fm = StudentRegistration()
    else :
        fm = StudentRegistration();
    studs = Student.objects.all();
    return render(request , 'enroll/addandshow.html' , {'form' : fm , 'stu' : studs})



# This function will update/edit
def update_data(request , id):
    if request.method == 'POST':
        pi = Student.objects.get(pk = id)
        fm = StudentRegistration(request.POST , instance = pi)
        if fm.is_valid():
            fm.save()
    else:
            pi = Student.objects.get(pk = id)
            fm = StudentRegistration(instance = pi)   
    return render(request , 'enroll/updatestudent.html' , {'form' : fm})




# This function will delete
def delete_data(request , id):
    if request.method == "POST":
        pi = Student.objects.get(pk= id)
        pi.delete()
        return HttpResponseRedirect('/')