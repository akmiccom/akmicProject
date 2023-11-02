from django.db import models
from config.settings import MARKDOWNX_MARKDOWN_EXTENSIONS
from markdown import markdown
from django.conf import settings
import os
from glob import glob

class MdToHtml(models.Model):
    
    title = models.CharField(verbose_name='Title', blank=False, null=False, max_length=128)
    markdown = models.TextField(verbose_name='markdown', blank=True, null=True, default='',)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def markdownToHtml(self):
        html = markdown(self.markdown, extensions=MARKDOWNX_MARKDOWN_EXTENSIONS,)
        return html
    
    # def update_or_craete_markdown(file):
    #     markdown_dir = os.path.join(settings.BASE_DIR, 'statisticsBlogs', 'markdown')
    #     for file in glob(f'{markdown_dir}/0101.md'):
    #         with open(file, 'r', encoding='utf-8') as f:
    #             markdown = f.read()
                
    #         MdToHtml.objects.update_or_create(
    #             title = 'インプットテスト',
    #             defaults={
    #                 'markdown': markdown,
    #                 },
    #         )