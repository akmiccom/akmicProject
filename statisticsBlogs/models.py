from django.db import models
from markdown import Markdown
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class StatisticsBlog(models.Model):
    
    chapter = models.CharField(
        verbose_name='Chapter',
        blank=False,
        null=False,
        max_length=64,
        )
    section = models.CharField(
        verbose_name='Section',
        blank=False,
        null=False,
        max_length=64,
        )
    title = models.CharField(
        verbose_name='Title',
        blank=False,
        null=False,
        max_length=128,
        )
    text = MarkdownxField(
        verbose_name='Text',
        blank=True,
        null=True,
        default=''
        )
    # MarkdownField変更によりコメントアウト
    # text = models.TextField(
    #     verbose_name='Text',
    #     blank=True,
    #     null=True,
    #     default=''
    #     )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    # markdownxの使用によりコメントアウト
    # def get_markdown_text_as_html(self):
    #     md = Markdown(extensions=['extra', 'admonition', 'sane_lists', 'toc', 'tables'])
    #     html = md.convert(self.text)
    #     return html
    
    def convert_markdown_to_html(self):
        return markdownify(self.text)
    

# class Post(models.Model):
#     title = models.CharField('title', max_length=255)
#     text = MarkdownxField('text')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at =models.DateTimeField(auto_now=True)

    
#     def __str__(self):
#         return self.title

#     def convert_markdown_to_html(self):
#         return markdownify(self.text)