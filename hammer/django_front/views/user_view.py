from django.views.generic import DetailView
from models.models import User



class UserView(DetailView):
    model = User
    template_name = "user_page.html"