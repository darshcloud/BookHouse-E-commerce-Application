from django.contrib import admin

# Register your models here.
from .models import Payment, Order, OrderBook

admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(OrderBook)