# Generated by Django 4.2.6 on 2023-10-12 07:11

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('statisticsBlogs', '0005_alter_statisticsblog_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statisticsblog',
            name='text',
            field=markdownx.models.MarkdownxField(blank=True, default='', null=True, verbose_name='Text'),
        ),
    ]