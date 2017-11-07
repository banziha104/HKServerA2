from django.contrib import admin
from .models import ContentType
# Register your models here.

class TypeAdmin(admin.ModelAdmin):
    list_display = ('types',)
    ordering = ['types']

admin.site.register(ContentType,TypeAdmin)