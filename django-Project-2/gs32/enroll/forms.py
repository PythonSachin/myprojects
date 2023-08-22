from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(label="MyName" , label_suffix=' ' , initial = 'Sachin' , required = 'False' , disabled=True);
