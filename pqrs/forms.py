# Django
from django import forms
# Crispy Forms
from crispy_forms.helper import FormHelper
# Models
from .models import *


class PQRForm(forms.ModelForm):
    """PQR Signup"""
    request_type = forms.ChoiceField(choices=PQR.REQUEST_TYPE_CHOICES, label='Selecciona el tipo de solicitud')

    class Meta:
        model = PQR
        fields = ['request_type', 'request_detail']
        widgets = {
            'request_detail': forms.Textarea(attrs={'placeholder': 'Describe tu solicitud aquí...'})
        }

    def __init__(self, *args, **kwargs):
        super(PQRForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False




