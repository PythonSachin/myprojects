from django.shortcuts import render
from datetime import date
# Create your views here.

posts = [
    {
     'slug' : 'hike in the mountains',
     'image': 'mountains.jpg',
     'author': 'Sachin',
     'date': date(2023 , 8 , 3),
     'title': "Mountain Hiking",
     'excerpt' : "here is nothing like the views you get when hiking in the mountains! and I wasn't even prepared for what happened whilst i was enjoying the view",
     'detail' :  '''Hello This is my first time making a site so i started with a 
        blogging site on which i have created using the templates of django 
        and i am quite excited to do this work.'''
    }
]
    

def starting_page(request):
    return render(request , "blog/welcome.html")

def posts(request):
    return render(request , "blog/all-posts.html")

def post_detail(request , slug):
    return render(request , 'blog/post_detail.html')