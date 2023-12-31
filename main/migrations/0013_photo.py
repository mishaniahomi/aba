# Generated by Django 4.2.1 on 2023-09-11 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_post_content_alter_post_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='galery', verbose_name='Фотография')),
                ('describe', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Фотографию',
                'verbose_name_plural': 'Фотографии',
                'ordering': ['-pk'],
            },
        ),
    ]
