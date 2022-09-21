from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from .models import Book
from category.models import category
from carts.models import CartItem
from django.db.models import Q
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse 



# Create your views here.

def store(request, category_slug=None):
    book_categories = None
    books = None

    if category_slug is not None:
        book_categories = get_object_or_404(category, slug=category_slug)
        books = Book.objects.filter(book_category=book_categories, is_available=True)
        paginator = Paginator(books, 2)
        page = request.GET.get('page')
        paged_books = paginator.get_page(page)
        books_count = books.count()
    else:
        books = Book.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(books, 6)
        page = request.GET.get('page')
        paged_books = paginator.get_page(page)
        books_count = books.count()

    context = {
        'books': paged_books,
        'books_count': books_count,
    }
    return render(request, 'store/store.html', context)


def book_detail(request, category_slug,book_slug):
    try:
        single_book= Book.objects.get(book_category__slug=category_slug,slug=book_slug)
        in_cart=CartItem.objects.filter(cart__cart_id=_cart_id(request),book=single_book).exists()
        

        
      
    except Exception as e:
        raise e

    context= {
        'single_book':single_book,
        'in_cart' : in_cart,
    }

    return render(request,'store/book_detail.html',context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:

            books = Book.objects.order_by('-creation_date').filter(Q(book_description__icontains=keyword) | Q(book_name__icontains=keyword))
            print(books)
            books_count = books.count()
    context = {
        'books':books,
        'books_count': books_count,
         }       
    return render(request,'store/store.html',context)
