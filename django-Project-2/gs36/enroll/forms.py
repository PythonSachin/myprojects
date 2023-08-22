from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(min_length = 10 , max_length = 100 , strip = True , empty_value= 'sachin'  , error_messages={'required' : 'Enter Your Name'});
    roll = forms.IntegerField(min_value = 4);
    price = forms.DecimalField(min_value = 4 , max_value=20 , max_digits=4 , decimal_places=2);
    agree = forms.BooleanField(label_suffix=' ' , label = 'I Agree');