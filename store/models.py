from django.db import models
from category.models import category
from django.urls import reverse


# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    book_description = models.TextField(max_length=500, blank=True)
    book_price = models.IntegerField()
    book_image = models.ImageField(upload_to='photos/products')
    book_stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    book_category = models.ForeignKey(category, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('book_detail', args=[self.book_category.slug, self.slug])

    def __str__(self):
        return self.book_name


class BookFormatManager(models.Manager):
    def bookformat(self):
        return super(BookFormatManager, self).filter(book_variation='format', is_active=True)


book_variation_choice = (
    ('format', 'format'),
)


class BookFormat(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_variation = models.CharField(max_length=100, choices=book_variation_choice)
    book_format_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now=True)

    objects = BookFormatManager()

    def __str__(self):
        return self.book_format_value
