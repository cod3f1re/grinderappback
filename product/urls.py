from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_overview, name='home'),
    path('createProduct/', views.add_products, name='add-items'),
    path('createCategory/', views.add_category, name='add-category')
]
