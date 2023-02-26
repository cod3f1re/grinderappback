from rest_framework import viewsets
from .serializers import UserSerializers
from .models import Users


class UserViewSets(viewsets.ModelViewSet):
	queryset = Users.objects.all()
	serializer_class = UserSerializers
