from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        User = get_user_model()
        model = User
        fields = '__all__'
