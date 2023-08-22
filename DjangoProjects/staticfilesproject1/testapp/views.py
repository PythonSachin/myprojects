from django.shortcuts import render
import datetime
# Create your views here.
def date_time_view(request):
    date = datetime.datetime.now();
    hrs = int(date.strftime('%H'));
    if hrs < 12:
        msg = "Hello Guest very good morning";
    elif hrs < 16:
        msg = "Hello Guest very good afternoon";
    elif hts < 21:
        msg = "Hello Guest very good evening";
    else :
        msg = "Hello Guest good night";
    my_dict = {'msg' : msg , 'date' : date};
    return render(request , 'testapp/results.html' , my_dict)