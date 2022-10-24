from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404
from store.models import Book, BookFormat
from django.core.exceptions import ObjectDoesNotExist

from .models import Cart, CartItem
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, book_id):
    book = Book.objects.get(id=book_id)  # get the book
    book_formats = []
    if request.method == 'POST':
        for item in request.POST:
            key = item
            value = request.POST[key]
            print(key, value)

            try:
                book_format = BookFormat.objects.get(book=book, book_variation__iexact=key,
                                                     book_format_value__iexact=value)
                # list of book formats
                book_formats.append(book_format)
            except:
                pass

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))  # get the cart using cart_id present in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()

    is_cart_item_exists = CartItem.objects.filter(book=book, cart=cart).exists()
    if is_cart_item_exists:
        cart_item = CartItem.objects.filter(book=book, cart=cart)
        # existing book formats -> database
        # current book format -> book_formats
        # item_id -> database
        existing_bookformat_list = []
        id = []
        for item in cart_item:
            existing_bookformat = item.book_format.all()
            existing_bookformat_list.append(list(existing_bookformat))
            id.append(item.id)

        print(existing_bookformat_list)

        if book_formats in existing_bookformat_list:
            # increase the cart item quantity
            index = existing_bookformat_list.index(book_formats)
            item_id = id[index]
            item = CartItem.objects.get(book=book, id=item_id)
            item.quantity += 1;
            item.save()
        else:
            item = CartItem.objects.create(book=book, quantity=1, cart=cart)
            if len(book_formats) > 0:
                item.book_format.clear()
                item.book_format.add(*book_formats)
            item.save()
    else:
        cart_item = CartItem.objects.create(
            book=book,
            quantity=1,
            cart=cart,
        )
        if len(book_formats) > 0:
            cart_item.book_format.clear()
            cart_item.book_format.add(*book_formats)
        cart_item.save()
    return redirect('cart')


def remove_cart(request, book_id, cart_item_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    book = get_object_or_404(Book, id=book_id)
    try:
        cart_item = CartItem.objects.get(book=book, cart=cart, id=cart_item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect('cart')


def remove_cart_item(request, book_id, cart_item_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    book = get_object_or_404(Book, id=book_id)
    cart_item = CartItem.objects.get(book=book, cart=cart, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')


def cart(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.book.book_price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total) / 100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/cart.html', context)


@login_required(login_url='login')
def checkout(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.book.book_price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total) / 100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/checkout.html', context)
