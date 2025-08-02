from models.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserService:
    def create_user(self, phone_number,password):
        if User.objects.filter(phone_number=phone_number).exists():
            return None
        user = User.objects.create(
            phone_number=phone_number
        )
        user.set_password(password)
        user.save()
        refresh = RefreshToken.for_user(user)
        return (str(refresh), str(refresh.access_token))
    def get_user(self, id):
        user = User.objects.get(id=id)
        return user
