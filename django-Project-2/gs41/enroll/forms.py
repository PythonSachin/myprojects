from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(error_messages={'required' : 'Name is required'})
    email = forms.EmailField(error_messages={'required' : 'Email is required'})
    password = forms.CharField(error_messages={'required' : 'password is required'})
    
