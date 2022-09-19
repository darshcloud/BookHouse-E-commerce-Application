from tabnanny import verbose
from django.db import models

from django.utils import timezone
from django.urls import reverse

# Create your models here.
class category(models.Model):
    category_name = models.SlugField(max_length=50,unique=True)
    slug = models.CharField(max_length=100,unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank =True)
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('books_by_category', args=[self.slug])
    
    def __str__(self):
        return self.category_name




# Create your models here.
