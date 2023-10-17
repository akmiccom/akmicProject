# Generated by Django 4.2.6 on 2023-10-17 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TravelBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', editable='Title', max_length=128, verbose_name='Title')),
                ('author', models.CharField(default='Anonymous', max_length=128, verbose_name='Author')),
                ('category', models.CharField(default='Other', max_length=128, verbose_name='Category')),
                ('text', models.TextField(blank=True, verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
