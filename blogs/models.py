from django.db import models
from markdown import Markdown

class Blog(models.Model):
    
    title = models.CharField(
        verbose_name='Title',
        blank=False,
        null=False,
        default='',
        editable='Title',
        max_length=128,
        help_text='',
        # unique=True,
        )
    author = models.CharField(verbose_name='Author', max_length=128, default='Anonymous')
    category = models.CharField(verbose_name='Category', max_length=128, default='Other')
    text = models.TextField(verbose_name='Text', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_markdown_text_as_html(self):
        md = Markdown(extensions=['extra', 'admonition', 'sane_lists', 'toc', 'tables', 'fenced_code'])
        html = md.convert(self.text)
        return html