# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
# Models
from .models import *
# Forms
from .forms import *


class PQRCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """PQR Create View"""
    model = PQR
    template_name = 'pqrs/PQRForm.html'
    form_class = PQRForm
    success_message = 'Solicitud creada exitosamente!'
    success_url = reverse_lazy('pqr_index')

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)


class PQRListView(SuccessMessageMixin, LoginRequiredMixin, ListView):
    """PQR Create View"""
    model = PQR
    template_name = 'pqrs/PQRList.html'
    queryset = 'pqrs'
