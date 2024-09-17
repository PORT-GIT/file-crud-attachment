from django.contrib import admin
from .models import Filelog, Filemovement

# Register your models here.
admin.site.register(Filelog)
admin.site.register(Filemovement)