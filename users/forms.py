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
    code = forms.CharField(required=False, )
    identification = forms.IntegerField(min_value=0)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'identification', 'password', 'code']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean(self):
        email = self.cleaned_data.get('email')
        identification = self.cleaned_data.get('identification')
        if User.objects.filter(email=email).exists():
            # Verifica si ya existe un usuario con ese email
            raise ValidationError({'email': ["Ya existe un usuario con ese correo"]})
        # if User.objects.filter(identification=identification).exists():
        #     # Verifica si ya existe un usuario con esa identificación
        #     raise ValidationError({'identification': ["Ya existe un usuario con esa identificación"]})
        print(self.errors)
        return self.cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email
        user.is_client = True
        user.set_password(self.cleaned_data['password'])
        # Si ingresa un código de referencia
        if user.code:
            # Encuentra el cliente asociado al código y le suma un punto
            client = User.objects.filter(code=user.code).first()
            client.current_points += 1
            client.save()
            user.code = ''

        if commit:
            user.save()
            # We have the primary key (ID Field) now so let's grab it
            id_string = str(user.id)
            random_str = self.generate_code()
            # Append the ID to the end of the random string
            code = (random_str + id_string)[-8:]
            while User.objects.filter(code=code).first():
                random_str = self.generate_code()
                code = (random_str + id_string)[-8:]
            user.code = code
            # Save the class instance
            user.save()
        return user

    def generate_code(self):
        # Define our random string alphabet (notice I've omitted I,O,etc. as they can be confused for other characters)
        upper_alpha = "ABCDEFGHJKLMNPQRSTVWXYZ"
        # Create an 8 char random string from our alphabet
        random_str = "".join(secrets.choice(upper_alpha) for i in range(8))
        return random_str


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label='Nombres')
    last_name = forms.CharField(required=True, label='Apellidos')
    email = forms.EmailField(disabled=True, widget=forms.TextInput(attrs={'readonly':'readonly'}), label='Correo electronico')
    avatar = forms.ImageField(allow_empty_file=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'avatar']