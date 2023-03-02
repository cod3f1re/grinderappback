from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .serializers import UserSerializers


class UserViewSets(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializers
