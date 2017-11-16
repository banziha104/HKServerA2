from django.contrib import admin
from HKDataBase.models import HKData
# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ('title','section','type','lat','lon','image','created','hit','writer')
    list_filter = ('section','created')
    search_fields = ('section','title')
    ordering = ['section']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.writer = request.user
        obj.save()


admin.site.register(HKData,DataAdmin)