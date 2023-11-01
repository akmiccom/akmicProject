from django.contrib import admin
from mdToHtml.models import MdToHtml


class MdToHtmlAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_display_links = ('title',)

admin.site.register(MdToHtml, MdToHtmlAdmin)
