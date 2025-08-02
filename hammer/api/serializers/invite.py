from rest_framework import serializers
from models.models import User

class UserInviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('invite_code','phone_number')