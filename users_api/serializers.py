from rest_framework import serializers

from .models import User, Item


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user_id.first_name')
    class Meta:
        model = Item
        fields = "__all__"

