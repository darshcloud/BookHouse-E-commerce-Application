from django.shortcuts import render
from store.models import Book, ReviewRating


def home(request):
    books = Book.objects.all().filter(is_available=True).order_by('creation_date')

    # Get the reviews
    for book in books:
        reviews = ReviewRating.objects.filter(book_id=book.id, status=True)

    context = {
        'books': books,
        'reviews': reviews,
    }
    return render(request, 'home.html', context)