# Generated by Django 4.2.1 on 2023-09-23 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_pagecontent_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagecontent',
            name='image',
        ),
        migrations.AddField(
            model_name='importantinfo',
            name='image',
            field=models.ImageField(default=1, upload_to='important_info/', verbose_name='Главная картинка'),
            preserve_default=False,
        ),
    ]
