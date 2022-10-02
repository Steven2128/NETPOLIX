# Django
from django.contrib import admin
# Models
from .models import *

admin.site.register(Film)
admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Classification)
admin.site.register(Serie)
admin.site.register(Collection)

