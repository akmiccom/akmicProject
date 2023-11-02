from django.db import models
from config.settings import MARKDOWNX_MARKDOWN_EXTENSIONS
from markdown import markdown
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class StatisticsBlog(models.Model):
    
    chapter = models.CharField(verbose_name='Chapter', blank=False, null=False, max_length=64,)
    section = models.CharField(verbose_name='Section', blank=False, null=False, max_length=64,)
    title = models.CharField(verbose_name='Title', blank=False, null=False, max_length=128,)
    markdown = MarkdownxField(verbose_name='Text', blank=True, null=True, default='',)
    # 追加予定反映されていない
    category = models.CharField(verbose_name='Category', blank=True, null=True, max_length=128,)
    author = models.CharField(verbose_name='Author', blank=True, null=True, max_length=128,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    # def convert_markdown_to_html(self):
    #     return markdownify(self.text)
    
    def markdownToHtml(self):
        html = markdown(self.markdown, extensions=MARKDOWNX_MARKDOWN_EXTENSIONS,)
        return html