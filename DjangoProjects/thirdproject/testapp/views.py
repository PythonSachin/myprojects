from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def good_morning_view(request):
    return HttpResponse('<h1>Hello friend good morning</h1>');

def good_afternoon_view(request):
    return HttpResponse('<h1>Hello friend good afternoon</h1>');

def good_evening_view(request):
    return HttpResponse('<h1>Hello friend good evening</h1>');
