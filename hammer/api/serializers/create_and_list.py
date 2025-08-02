from rest_framework import serializers
from models.models import User

class UserCreateAndListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone_number','password')