from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from accounts.forms import UserAuthenticationForm


class HomeView(View):
    template_name = "home.html"

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = "login.html"
    authentication_form = UserAuthenticationForm
    success_message = "You've logged in successfully"
    next_page = reverse_lazy('home')
