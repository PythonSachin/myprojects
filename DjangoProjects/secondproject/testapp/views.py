from django.http import HttpResponse
import datetime
# Create your views here.
def current_server_time(request):
    time = datetime.datetime.now()
    s = "The Current date and time at server is: " + str(time);
    return HttpResponse(s);