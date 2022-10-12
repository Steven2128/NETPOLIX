# Django
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Forms
from users.forms import SignupForm


class LoginView(LoginView):
    """Login View"""
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        self.object = None
        return super().get(request, *args, **kwargs)

class SignupView(CreateView):
    """Signup View"""
    model = User
    form_class = SignupForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('film-list')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        self.object = None
        return super().get(request, *args, **kwargs)
