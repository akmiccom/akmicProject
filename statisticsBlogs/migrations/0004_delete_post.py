# Generated by Django 4.2.5 on 2023-10-04 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statisticsBlogs', '0003_alter_statisticsblog_text'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
