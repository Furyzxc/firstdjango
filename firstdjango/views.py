from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Book
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookForm
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'homepage/index.html')

def contactus(request):
    return render(request, 'contactus/index.html')

def viewbooks(request):
    context = {'books': Book.objects.all() }
    return render(request, 'book_list/index.html', context)

def view_single_book(request, bookid):
    by_id = get_object_or_404(Book, id=bookid)
    context = {"book": by_id}

    return render(request, 'book/index.html', context)

def search_book(request):
    query = request.GET.get('q')
    
    if not query:   
        books = Book.objects.none()
    else:
        books = Book.objects.filter(title__icontains=query)
    
    return render(request, "search/index.html", {"books": books})

def view_books_by_year(request, year):
    by_year = Book.objects.filter(year=year)
    context = {'books': by_year}
    return render(request, 'base/index.html', context)

def view_books_by_category(request, category):
    by_category = Book.objects.all() if category.lower() == 'default' else Book.objects.filter(category=category)
    context = {'books': by_category}
    return render(request, 'base/index.html', context)

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.added_by = request.user
            book.save()
            return redirect('books')
    else:
        form = BookForm()

    return render(request, 'addbook/index.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/registration.html', {'form': form})