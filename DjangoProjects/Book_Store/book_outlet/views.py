from django.shortcuts import render
from book_outlet.models import Book
from django.http import Http404

# Create your views here.

def index(request):
    books  = Book.objects.all()
    return render(request , 'book_outlet/index.html' , {'books' : books})

def book_detail(request, slug):
    try:
       book = Book.objects.get(slug=slug)
    except :
        raise Http404()
    data = {        
            'title': book.title,
            'author': book.author,
            'rating': book.rating,
            'bestseller': book.is_bestselling      
          }   
    context = {'data':data}
    return render(request , 'book_outlet/book_detail.html' , context=context
          
         )

