# Generated by Django 4.2.6 on 2023-11-02 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statisticsBlogs', '0007_rename_text_statisticsblog_markdown_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statisticsblog',
            name='author',
        ),
        migrations.RemoveField(
            model_name='statisticsblog',
            name='category',
        ),
    ]
