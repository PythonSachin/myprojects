from django.urls import path
from . import views

urlpatterns = [
    # path("january" , views.jan),
    # path("february" , views.feb),
    # path("march" , views.mar)
    
    path("" , views.index , name = "index"),
    path("<int:month>" , views.monthly_challenge_by_num),
    path("<str:month>" , views.monthly_challenge , name = "month-challenge"),
]