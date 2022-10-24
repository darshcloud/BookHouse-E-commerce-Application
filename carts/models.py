from django.db import models
from store.models import Book, BookFormat


# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_format = models.ManyToManyField(BookFormat, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.book.book_price * self.quantity

    def __unicode__(self):
        return self.book
