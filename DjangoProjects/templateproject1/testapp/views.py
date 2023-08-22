from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def template_view(request):
     
     #  return render(request , 'testapp/results.html');
     dt = datetime.datetime.now();
     my_dict = {'date' : dt}
    #  return render(request , 'testapp/results.html' , context = my_dict);
     return render(request , 'testapp/results.html' , my_dict);