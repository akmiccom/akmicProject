from django.contrib import admin
from travelBlogs.models import TravelBlog


class TravelBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'updated_at')
    list_display_links = ('title',)

admin.site.register(TravelBlog, TravelBlogAdmin)