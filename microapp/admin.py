from django.contrib import admin
from microapp.models import *

# Register your models here.
admin.site.register(contact_table)

# admin.site.register(File)

class FileAdmin(admin.ModelAdmin):
    list_display = ['file']