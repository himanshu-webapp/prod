from django.contrib import admin
from .models import BlogPost,BlogComment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class BlogPostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)

admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(BlogComment)