from django.db import models
from markdownx.models import MarkdownxField
from markdown import Markdown
from markdownx.utils import markdownify

class TravelBlog(models.Model):
    
    title = models.CharField(verbose_name='Title', blank=False, null=False, default='', editable='Title', max_length=128, help_text='',)
    author = models.CharField(verbose_name='Author', max_length=128, default='Anonymous')
    category = models.CharField(verbose_name='Category', max_length=128, default='Other')
    text = MarkdownxField(verbose_name='Text', blank=True, null=True, default='',)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def convert_markdown_to_html(self):
        return markdownify(self.text)