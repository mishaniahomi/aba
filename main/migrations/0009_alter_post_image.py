# Generated by Django 4.2.1 on 2023-09-06 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_ourpartners_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='news_image/', verbose_name='Изображение партнера'),
        ),
    ]
