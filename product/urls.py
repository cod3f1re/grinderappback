from django.urls import path

from . import views

urlpatterns = [
    path('', views.sample_api, name='index')
]
