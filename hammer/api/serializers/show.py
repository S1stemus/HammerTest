from rest_framework import serializers
from models.models import User
from .show_user import UserShowOnlySerializer

class UserShowSerializer(serializers.ModelSerializer):
    users=serializers.SerializerMethodField()
    def get_users(self, obj):
        users = User.objects.filter(used_invite_code=obj.invite_code)
        return UserShowOnlySerializer(users, many=True).data
    class Meta:
        model = User
        fields = ('id', 'phone_number', 'invite_code', 'used_invite_code','users')