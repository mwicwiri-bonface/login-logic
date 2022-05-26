from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from accounts.forms import UserAuthenticationForm


class HomeView(TemplateView):
    template_name = "home.html"


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = "login.html"
    authentication_form = UserAuthenticationForm
    success_message = "You've logged in successfully"
    next_page = reverse_lazy('home')
