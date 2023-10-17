from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class StatisticsBlog(models.Model):
    
    chapter = models.CharField(verbose_name='Chapter', blank=False, null=False, max_length=64,)
    section = models.CharField(verbose_name='Section', blank=False, null=False, max_length=64,)
    title = models.CharField(verbose_name='Title', blank=False, null=False, max_length=128,)
    text = MarkdownxField(verbose_name='Text', blank=True, null=True, default='',)
    # 追加予定
    # category = models.CharField(verbose_name='Category', blank=True, null=True, max_length=128,)
    # author = models.CharField(verbose_name='Author', blank=True, null=True, max_length=128,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    # MarkdownField変更によりコメントアウト
    # text = models.TextField(verbose_name='Text', blank=True, null=True, default='' )

    def __str__(self):
        return self.title
    
    def convert_markdown_to_html(self):
        return markdownify(self.text)
    