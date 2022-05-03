from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Todo)

class DisplayAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')