from django import forms
from .models import Student

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name' , 'email' , 'password']


        
class TeacherRegistration(StudentRegistration):
    class Meta(StudentRegistration.Meta):
        model = Student
        fields = ['teacher_name' , 'email' , 'password']

