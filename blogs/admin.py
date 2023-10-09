from django.contrib import admin
from blogs.models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'updated_at')
    list_display_links = ('title',)

admin.site.register(Blog, BlogAdmin)
