from django.contrib import admin
from statisticsBlogs.models import StatisticsBlog
from markdownx.admin import MarkdownxModelAdmin

    
class MarkdownxModelAdmin(admin.ModelAdmin):
    list_display = ('chapter', 'section', 'title', 'created_at', 'updated_at',
                    # 'category', 'author',
                    )
    list_display_links = ('title',)
    
    
admin.site.register(StatisticsBlog, MarkdownxModelAdmin)