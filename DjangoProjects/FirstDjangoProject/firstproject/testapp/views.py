from django.http import HttpResponse

# Create your views here.
def hello_world_view(request):
    return HttpResponse('<h1>Hello! This is response from django application</h1>');
