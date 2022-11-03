from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, get_object_or_404,redirect
from .models import Book,ReviewRating
from category.models import category
from carts.models import CartItem
from django.db.models import Q
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse 
from .forms import ReviewForm
from django.contrib import messages
from orders.models import OrderBook


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
    
    if request.user.is_authenticated:
        
    
        try:
            orderbook=OrderBook.objects.filter(user=request.user,book_id=single_book.id).exists()
        except OrderBook.DoesNotExist:
            orderbook=None
    else:
        orderbook=None   
        #get average review
    reviews=ReviewRating.objects.filter(book_id=single_book.id,status=True)  
        
        
    context= {
        'single_book':single_book,
        'in_cart' : in_cart,
        'orderbook': orderbook,
        'reviews':reviews,
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

def submit_review(request,book_id):
    url=request.META.get('HTTP_REFERER')
    #print(">>>>>>>>>>>>>>>"+ str(book_id)+ "    "+ str(request.user.id))
    if request.method=='POST':
        try:
            reviews=ReviewRating.objects.get(user__id=request.user.id,book__id=book_id)
            #print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"+reviews)
            form= ReviewForm(request.POST,instance=reviews)
            res=form.save()
            #print("form result"+res)
            messages.success(request,'Thank you! Your review has been updated')
            return redirect(url)
        
        except ReviewRating.DoesNotExist:
            form=ReviewForm(request.POST)
            if form.is_valid():
                data=ReviewRating()
                data.subject=form.cleaned_data['subject']
                data.rating=form.cleaned_data['rating']
                data.review=form.cleaned_data['review']
                data.ip=request.META.get('REMOTE_ADDR')
                data.book_id=book_id
                data.user_id=request.user.id
                data.save()
                messages.success(request,'Thank you! Your review has been submitted')
                return redirect(url)
                
            
            
            
        
    
