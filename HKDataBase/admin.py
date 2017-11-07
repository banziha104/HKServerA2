from django.contrib import admin
from HKDataBase.models import HKData
# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ('title','section','type','lat','lon','image','created')
    list_filter = ('section','created')
    search_fields = ('section','title')
    ordering = ['section']

admin.site.register(HKData,DataAdmin)