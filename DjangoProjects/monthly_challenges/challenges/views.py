from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january" : "Eat lots of meat in january",
    "february" : "Eat only chicken in february",
    "march" : "Eat egg rolls in march",
    "april" : "Eat momos in april",
    "may" : "Eat only fish curry and roti in may",
    "june" : "Just chill in ac because too hot",
    "july" : "work to the bone in this month",
    "august" : "get salary and have fun",
    "september" : "Eat lots of chicken biryani",
    "october" : "Eat lots of samosa chaat",
    "november" : "only simple bhojan",
    "december" : None
}
# Create your views here.

# def jan(request):
#     return HttpResponse("This Works!")

# def feb(request):
#     return HttpResponse("This also Works!")

# def mar(request):
#     return HttpResponse("This too Works!")

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys());
    return render(request , "challenges/index.html" , {
        'months' : months
    })


def monthly_challenge_by_num(request , month):
    months = list(monthly_challenges.keys());
    redirected_month = months[month - 1];
    redirect_path = reverse("month-challenge" , args = [redirected_month]);
    return HttpResponseRedirect(redirect_path);

def monthly_challenge(request , month):
    try:
       challenge_text = monthly_challenges[month];
    #    response_data = f"<h1>{challenge_text}</h1>"
    #    return HttpResponse(challenge_text)

       return render(request , "challenges/challenge.html" , {'text' : challenge_text , 'Month' : month})
    except:
       raise Http404()

