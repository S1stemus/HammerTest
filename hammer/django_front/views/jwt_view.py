from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
import time


class JwtView(View):
    template_name = "jwt.html"

    def get(self, request):
        time.sleep(2)
        return render(request, self.template_name)

    def post(self, request):
        return JsonResponse({"message": "success"})
