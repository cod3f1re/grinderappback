from rest_framework import serializers

from users.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['is_removed', 'created', 'modified']
