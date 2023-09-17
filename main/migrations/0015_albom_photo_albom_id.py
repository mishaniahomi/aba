# Generated by Django 4.2.1 on 2023-09-12 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_photo_describe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Albom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название альбома')),
                ('date', models.DateField(verbose_name='Дата создания')),
                ('picture', models.ImageField(upload_to='', verbose_name='Обожка')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
                'ordering': ['date'],
            },
        ),
        migrations.AddField(
            model_name='photo',
            name='albom_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.albom', verbose_name='Альбом'),
        ),
    ]