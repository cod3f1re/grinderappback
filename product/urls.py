from django.urls import path
from product.views import Products, Categories

urlpatterns = [
    path('', Products.as_view(), name='add-items'),
    path('categories', Categories.as_view(), name='add-category')
]
