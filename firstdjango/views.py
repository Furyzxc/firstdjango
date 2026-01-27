from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'homepage/index.html')

def contactus(request):
    return render(request, 'contactus/index.html')

def viewbooks(request):
    context = {'books': Book.objects.all() }
    return render(request, 'base/index.html', context)

def view_single_book(request, bookid):
    by_id = get_object_or_404(Book, id=bookid)
    context = {"book": by_id}

    return render(request, 'book/index.html', context)

def view_books_by_year(request, year):
    by_year = Book.objects.filter(year=year)
    context = {'books': by_year}
    return render(request, 'base/index.html', context)

def view_books_by_category(request, category):
    by_category = Book.objects.all() if category.lower() == 'default' else Book.objects.filter(category=category)
    context = {'books': by_category}
    return render(request, 'base/index.html', context)