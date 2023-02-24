from django.urls import path
from .views import *

app_name = 'users'
urlpatterns = [
    path('', PostApiView.as_view()),
    path('createuser/', CreateUser.as_view()),
    path('<int:pk>/', PostAPIViewDetail.as_view()),
]