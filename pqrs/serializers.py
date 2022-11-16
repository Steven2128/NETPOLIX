# DRF
from rest_framework import serializers
# Models
from .models import *


class PQRSerializer(serializers.ModelSerializer):
    class Meta:
        model = PQR
        fields = '__all__'
