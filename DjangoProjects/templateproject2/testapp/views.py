from django.shortcuts import render
import datetime

# Create your views here.

def wish_view(request):
    date = datetime.datetime.now();
    hrs = int(date.strftime('%H'))
    msg = "Hello! A very good ";
    if(hrs < 12):
        msg = msg + "morning!!!";
    elif hrs < 16:
        msg = msg + "afternoon!!!";
    elif hrs < 21:
        msg = msg + "evening!!!";
    else :
        msg = msg + "night!!!";

    response = render(request , 'testapp/results.html', {'msg' : msg , 'date' : date});
    return response;
