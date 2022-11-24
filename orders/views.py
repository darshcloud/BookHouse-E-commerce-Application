from http.client import HTTPResponse
from locale import currency
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import datetime
import json

from carts.models import CartItem
from .forms import OrderForm
from .models import Order, Payment, OrderBook
from store.models import Book
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def payments(request):
    body = json.loads(request.body)
    order = Order.objects.get(user=request.user, is_ordered=False, order_number=body['orderID'])
    # store transaction details inside payment model
    payment = Payment(
        user=request.user,
        payment_id=body['transID'],
        payment_method=body['payment_method'],
        amount_paid=order.order_total,
        status=body['status'],
    )
    payment.save()
    order.payment = payment
    order.is_ordered = True
    order.save()

    # Move the cart items to Order Book table
    cart_items = CartItem.objects.filter(user=request.user)

    for item in cart_items:
        orderbook = OrderBook()
        orderbook.order_id = order.id
        orderbook.payment = payment
        orderbook.user_id = request.user.id
        orderbook.book_id = item.book_id
        orderbook.quantity = item.quantity
        orderbook.book_price = item.book.book_price
        orderbook.ordered = True
        orderbook.save()

        cart_item = CartItem.objects.get(id=item.id)
        book_format = cart_item.book_format.all()
        orderbook = OrderBook.objects.get(id=orderbook.id)
        orderbook.book_format.set(book_format)
        orderbook.save()

        # Reduce the quantity of sold products
        book = Book.objects.get(id=item.book_id)
        book.book_stock -= item.quantity
        book.save()

    # Clear the cart
    CartItem.objects.filter(user=request.user).delete()

    # Send order receive email to customer
    mail_subject = 'Thank You for your Order!'
    message = render_to_string('orders/order_received_email.html', {
        'user': request.user,
        'order': order,
    })
    to_email = request.user.email
    send_email = EmailMessage(mail_subject, message, to=[to_email])
    send_email.send()

    # Send order number and transaction id back to sendData method via JsonResponse
    data = {
        'order_number': order.order_number,
        'transID': payment.payment_id,
    }
    return JsonResponse(data)

    return render(request, 'orders/payments.html')


# Create your views here.
def place_order(request, total=0, quantity=0, ):
    current_user = request.user

    # if cart item is null redirect to store
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store')

    grand_total = 0
    tax = 0
    for cart_item in cart_items:
        total += (cart_item.book.book_price * cart_item.quantity)
        quantity += cart_item.quantity
    tax = (2 * total) / 100
    grand_total = total + tax

    if request.method == 'POST':
        form = OrderForm(request.POST)
        # print(form.errors) #DEBUG
        # print("Is the form valid? : "+ str(form.is_valid())) # DEBUG
        if form.is_valid():
            # store info in order table
            data = Order()
            data.user = current_user
            # print("Current user is : " + str(current_user))  #DEBUG
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            # order num generation

            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr, mt, dt)
            current_date = d.strftime("%Y%m%d")
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

        order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)
        context = {
            'order': order,
            'cart_items': cart_items,
            'total': total,
            'tax': tax,
            'grand_total': grand_total,

        }
        return render(request, 'orders/payments.html', context)
    else:
        return redirect('checkout')


def order_complete(request):
    order_number = request.GET.get('order_number')
    transID = request.GET.get('payment_id')

    try:
        order = Order.objects.get(order_number=order_number, is_ordered=True)
        ordered_books = OrderBook.objects.filter(order_id=order.id)

        subtotal = 0
        for i in ordered_books:
            subtotal += i.book_price * i.quantity

        payment = Payment.objects.get(payment_id=transID)

        context = {
            'order': order,
            'ordered_books': ordered_books,
            'order_number': order.order_number,
            'transID': payment.payment_id,
            'payment': payment,
            'subtotal': subtotal,
        }
        return render(request, 'orders/order_complete.html', context)
    except(Payment.DoesNotExist, Order.DoesNotExist):
        return redirect('home')





