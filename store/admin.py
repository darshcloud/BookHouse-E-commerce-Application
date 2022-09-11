from django.contrib import admin
from .models import Book


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    display_list = ('book_name', 'book_price', 'book_stock', 'book_category', 'modified_date', 'is_available')
    prepopulated_fields = populated_fields = {'slug': ('book_name',)}


admin.site.register(Book, BookAdmin)
