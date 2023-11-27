# Generated by Django 4.2.1 on 2023-09-20 18:18

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_machine_preview_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner_akcii',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Основной контент'),
        ),
        migrations.AlterField(
            model_name='banner_akcii',
            name='href',
            field=models.TextField(blank=True, null=True, verbose_name='Ссылка на акцию'),
        ),
        migrations.AlterField(
            model_name='banner_akcii',
            name='short_description',
            field=models.TextField(blank=True, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание техники'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='preview_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Краткое описание техники'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
