# Generated by Django 4.2.1 on 2023-09-23 09:41

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_banner_akcii_content_alter_banner_akcii_href_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportantInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Важная информация',
                'verbose_name_plural': 'Важная информация',
            },
        ),
        migrations.CreateModel(
            name='PageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Контент страницы',
                'verbose_name_plural': 'Контенты страниц',
            },
        ),
    ]