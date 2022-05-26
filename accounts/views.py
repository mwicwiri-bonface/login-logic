from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

from accounts.forms import UserAuthenticationForm


class HomeView(TemplateView):
    template_name = "home.html"


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = "login.html"
    authentication_form = UserAuthenticationForm
    success_message = "You've logged in successfully"
    next_page = reverse_lazy('home')


class UserLogoutView(View):
    def get(self, *args, **kwargs):
        logout(self.request)
        messages.info(self.request, "You've logged out successfully.")
        return redirect("home")