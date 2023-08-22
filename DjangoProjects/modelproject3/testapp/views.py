from django.shortcuts import render
from testapp.models import Data
# Create your views here.


def get_country_info(request):
    data = Data.objects.all();
    return render(request , 'testapp/results.html' , {'data' : data})
