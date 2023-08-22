from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def greeting_view(request):
    return HttpResponse('<h1>Hello Friends good morning have a nice day</h1>');

