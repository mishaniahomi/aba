# Generated by Django 4.2.1 on 2023-11-30 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_post_picture_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='importantinfo',
            name='picture_url',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Расположение главного изображения'),
        ),
    ]
