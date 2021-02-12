from .views import CategoryList, \
    CategoryDetail, \
    BookList, \
    BookDetail, \
    ProductList, \
    ProductDetail
from django.urls import path

urlpatterns = [
    path('categories', CategoryList.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='single-category'),
    path('books', BookList.as_view(), name='books'),
    path('books/<int:pk>/', BookDetail.as_view(), name='single-book'),
    path('products', ProductList.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='single-product'),
]