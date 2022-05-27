import re

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView

from accounts.forms import UserAuthenticationAuthForm, ContactForm


class HomeView(TemplateView):
    template_name = "home.html"


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = "login.html"
    authentication_form = UserAuthenticationAuthForm
    success_message = "You've logged in successfully"
    next_page = reverse_lazy('home')


class UserLogoutView(View):
    def get(self, *args, **kwargs):
        logout(self.request)
        messages.info(self.request, "You've logged out successfully.")
        return redirect("home")


class ContactCreateView(SuccessMessageMixin, CreateView):
    form_class = ContactForm
    template_name = "contact-form.html"
    success_message = "Request has been sent successfully."
    success_url = reverse_lazy('hr:job-list')