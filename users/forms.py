# Django
from django import forms
# from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Models
from .models import *


class SignupForm(forms.ModelForm):
    """Form Signup"""
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            # Verifica si ya existe un usuario con ese email
            raise ValidationError({'email': ["Ya existe un usuario con ese correo"]})
        return self.cleaned_data


    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email
        user.is_client = True
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user