from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views import View
import time



class RegisterView(View):
    template_name = "register.html"

    def get(self, request):
        return render(request, self.template_name)

