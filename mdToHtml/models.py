from django.db import models
from config.settings import MARKDOWNX_MARKDOWN_EXTENSIONS
from markdown import markdown


class MdToHtml(models.Model):
    
    title = models.CharField(verbose_name='Title', blank=False, null=False, max_length=128)
    markdown = models.TextField(verbose_name='markdown', blank=True, null=True, default='',)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def markdownToHtml(self):
        html = markdown(self.markdown, extensions=MARKDOWNX_MARKDOWN_EXTENSIONS)
        return html
    