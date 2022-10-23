from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Greeting, Book

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, "index.html", context)

def insert(request):
    author_name = request.POST.get('author_name')
    book_name = request.POST.get('book_name')
    price = request.POST.get('price')
    release_date = request.POST.get('release_date')
    availability = False
    if request.POST.get('availability') == 'on': 
        availability = True
    book = Book(author_name = author_name, book_name = book_name, price = price,
        release_date = release_date, availability = availability)
    book.save()
    return HttpResponseRedirect('/')

def edit(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book}
    print (book)
    print (book.release_date)
    return render(request, 'edit.html', context)

def update(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.author_name = request.POST.get('author_name')
    book.book_name = request.POST.get('book_name')
    book.price = request.POST.get('price')
    book.release_date = request.POST.get('release_date')
    if request.POST.get('availability') == 'on': 
        book.availability = True
    else:
        book.availability = False
    book.save()
    return HttpResponseRedirect('/')

def delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return HttpResponseRedirect('/')




def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
