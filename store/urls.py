from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='books_by_category'),
    path('category<slug:category_slug>/<slug:book_slug>/', views.book_detail, name='book_detail'),
    path('search/', views.search, name= 'search'),
]


