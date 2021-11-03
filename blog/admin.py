from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'author', 'subject',
     'content'
    )

admin.site.register(Blog, BlogAdmin)

