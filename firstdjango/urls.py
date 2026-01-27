
from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('contactus', views.contactus, name="contactus"),
   path('books', views.viewbooks, name="books"),
   path('books/<int:bookid>', views.view_single_book, name='single_book'),
   path('books/year/<int:year>', views.view_books_by_year, name='books_by_year'),
   path('books/category/<str:category>', views.view_books_by_category, name='books_by_category')
]  