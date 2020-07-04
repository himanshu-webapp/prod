from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import ServiceCategory,ServiceImage,Service
# Register your models here.

class ServiceImageAdmin(admin.ModelAdmin):
    list_display = ('category_name','related_to_name','location','id')

class ServicesAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = ('name','slug','id')

admin.site.register(ServiceCategory)
admin.site.register(Service,ServicesAdmin)
admin.site.register(ServiceImage,ServiceImageAdmin)

