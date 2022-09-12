from django.shortcuts import render, get_object_or_404
from .models import Book
from category.models import category


# Create your views here.

def store(request, category_slug=None):
    book_categories = None
    books = None

    if category_slug is not None:
        book_categories = get_object_or_404(category, slug=category_slug)
        books = Book.objects.filter(book_category=book_categories, is_available=True)
        books_count = books.count()
    else:
        books = Book.objects.all().filter(is_available=True)
        books_count = books.count()

    context = {
        'books': books,
        'books_count': books_count,
    }
    return render(request, 'store/store.html', context)
