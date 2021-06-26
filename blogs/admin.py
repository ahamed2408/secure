from django.contrib import admin
from .models import analytics, orderss, shipd
# Register your models here.

My_models=[analytics, orderss, shipd]

admin.site.register(My_models)