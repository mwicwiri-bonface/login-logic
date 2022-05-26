from django.contrib import messages
from django.shortcuts import render
from django.views import View


class Login(View):
    template_name = "login.html"

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)
