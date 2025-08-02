from rest_framework import serializers
from models.models import User

class UserShowOnlySerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'phone_number', 'invite_code', 'used_invite_code')