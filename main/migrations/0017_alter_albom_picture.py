# Generated by Django 4.2.1 on 2023-09-12 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_albom_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albom',
            name='picture',
            field=models.ImageField(upload_to='albom', verbose_name='Обожка'),
        ),
    ]
