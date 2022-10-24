from django.contrib import admin
from .models import Book, BookFormat


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'book_price', 'book_stock', 'book_category', 'modified_date', 'is_available')
    prepopulated_fields = populated_fields = {'slug': ('book_name',)}


class BookVariationAdmin(admin.ModelAdmin):
    list_display = ('book', 'book_variation', 'book_format_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('book', 'book_variation', 'book_format_value')


admin.site.register(Book, BookAdmin)
admin.site.register(BookFormat, BookVariationAdmin)
