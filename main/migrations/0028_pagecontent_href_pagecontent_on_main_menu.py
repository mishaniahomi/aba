# Generated by Django 4.2.1 on 2023-09-30 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_buklet_sertificates'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagecontent',
            name='href',
            field=models.SlugField(blank=True, null=True, verbose_name='Отдельная ссылка'),
        ),
        migrations.AddField(
            model_name='pagecontent',
            name='on_main_menu',
            field=models.BooleanField(default=False),
        ),
    ]
