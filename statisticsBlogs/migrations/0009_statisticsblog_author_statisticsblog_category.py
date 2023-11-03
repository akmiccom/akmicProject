# Generated by Django 4.2.6 on 2023-11-02 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statisticsBlogs', '0008_remove_statisticsblog_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='statisticsblog',
            name='author',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='statisticsblog',
            name='category',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Category'),
        ),
    ]
