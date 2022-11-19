# Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
# DRF
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
# Serializers
from .serializers import *
# Forms
from .forms import SignupForm, ProfileForm
# Models Transactions
from transactions.models import Transaction


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


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = ProfileForm(request.POST, request.FILES, instance=request.user)
        # profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        # if user_form.is_valid() and profile_form.is_valid():
        if user_form.is_valid():
            user_form.save()
            # profile_form.save()
            # messages.success(request, 'Cuenta actualizada exitosamente!')
            return redirect('profile')
    else:
        user_form = ProfileForm(instance=request.user)
        # pro = Profile.objects.filter(user_id=request.user.id)
        # if not pro:
        #     profile = Profile(user=request.user)
        #     profile.save()
    context = {
        'u_form': user_form,
    }

    return render(request, 'users/profile.html', context)


class UserModelViewSet(viewsets.ModelViewSet):
    """User Model View Set"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsersWithMoreTransactions(viewsets.generics.ListAPIView):
    """
    Lista los 10 usuarios que más transacciones han realizado
    """
    queryset = User.objects.all().order_by('-amount_transactions')[:10]
    serializer_class = UserSerializer

