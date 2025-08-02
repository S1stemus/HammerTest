from django.urls import include, path

from django_front.views.jwt_view import JwtView
from django_front.views.register_view import RegisterView
from django_front.views.user_view import UserView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("jwt/", JwtView.as_view(), name="jwt"),
    path("user/<int:pk>/", UserView.as_view(), name="user"),
]
