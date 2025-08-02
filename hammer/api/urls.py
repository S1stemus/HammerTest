from api.views.user import UserCreateAndListView, UserShowView, UserInviteView

from django.urls import path


urlpatterns = [
    path('user/<int:pk>/', UserShowView.as_view()),
    path('users/', UserCreateAndListView.as_view()),
    path('invite/', UserInviteView.as_view()),
    
]
