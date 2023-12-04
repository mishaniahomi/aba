# Generated by Django 4.2.1 on 2023-11-30 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_importantinfo_picture_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='akcii',
            name='picture_url',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Расположение главного изображения'),
        ),
        migrations.AddField(
            model_name='albom',
            name='picture_url',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Расположение пути'),
        ),
        migrations.AddField(
            model_name='banner_akcii',
            name='picture_url',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Расположение пути'),
        ),
        migrations.AddField(
            model_name='categories',
            name='picture_url',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Расположение пути'),
        ),
        migrations.AddField(
            model_name='machine',
            name='picture_url',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Расположение главного изображения'),
        ),
        migrations.AddField(
            model_name='photo',
            name='picture_url',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Расположение пути'),
        ),
    ]