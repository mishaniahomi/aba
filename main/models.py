from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils import timezone


class Photo(models.Model):
    picture = models.ImageField(verbose_name='Фотография', upload_to='galery')
    describe = models.TextField(verbose_name='Описание')
    # albom_id = models.ForeignKey('Albom', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Альбом')

    class Meta:
        verbose_name = 'Фотографию'
        verbose_name_plural = 'Фотографии'
        ordering = ['-pk']


class banner_akcii(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название акции')
    image = models.ImageField(verbose_name='Главное изображение', upload_to='banner')
    short_description = models.TextField(verbose_name='Краткое описание')
    content = RichTextUploadingField(verbose_name='основной контент')
    href = models.TextField(verbose_name="ссылка на акцию", blank=True, null=True)

    class Meta:
        verbose_name = 'Банер'
        verbose_name_plural = 'Банеры'

    def __str__(self) -> str:
        return self.title


class Categories(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название категории')
    icon = models.ImageField(verbose_name='Иконка категории', upload_to='categoties_icons')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Родительская категория')
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

class Machine(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название техники')
    main_image = models.ImageField(verbose_name='Главное изображение техники', upload_to='machine')
    description = RichTextUploadingField(verbose_name='Описание техники')
    categories_id = models.ForeignKey('Categories', on_delete=models.CASCADE)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техники'

    def __str__(self) -> str:
        return self.name

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'slug': self.slug})


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = RichTextUploadingField(verbose_name='Описание')
    image = models.ImageField(verbose_name="Главная картинка новости", upload_to='news_image/')
    created_at = models.DateField(default=timezone.now, verbose_name='Дата создания')
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at', 'title']

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('postdetailview', kwargs={'slug': self.slug})


class OurPartners(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя партнера")
    image = models.ImageField(verbose_name="Изображение партнера", upload_to='partner_logos/')
    href = models.TextField(verbose_name="ссылка на партнера", blank=True, null=True)

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

    def __str__(self) -> str:
        return self.name
