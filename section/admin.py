from django.contrib import admin
from section.models import Section
# Register your models here.


class SectionAdmin(admin.ModelAdmin):
    list_display = ('section_name','lat','lon')
    ordering = ['section_name']


admin.site.register(Section, SectionAdmin)