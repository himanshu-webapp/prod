from django.contrib import admin
from .models import Certificate,InternshipApplication,JobApplication

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('certificateno','name','dateofissue')

class JobAdmin(admin.ModelAdmin):
    list_display = ('name','profile_applying_for','resume')

class InternAdmin(admin.ModelAdmin):
    list_display = ('name','profile_applying_for','resume')

admin.site.register(JobApplication,JobAdmin)
admin.site.register(Certificate,CertificateAdmin)
admin.site.register(InternshipApplication,InternAdmin)