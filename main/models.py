from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils import timezone
from PIL import Image
import datetime


class Albom(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название альбома')
    date = models.DateField(verbose_name='Дата создания')
    picture = models.ImageField(verbose_name='Обожка', upload_to='albom')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField()
    picture_url = models.CharField(max_length=200, verbose_name='Расположение пути', blank=True, null=True) 

    def save(self, *args, **kwargs):
        self.picture_url = self.picture.url
        super().save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('albomDetail', kwargs={'slug': self.slug})


class Photo(models.Model):
    picture = models.ImageField(verbose_name='Фотография', upload_to='galery')
    describe = models.TextField(verbose_name='Описание', null=True, blank=True)
    albom_id = models.ForeignKey('Albom', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Альбом')
    picture_url = models.CharField(max_length=200, verbose_name='Расположение пути', blank=True, null=True) 

    def save(self, *args, **kwargs):
        self.picture_url = self.picture.url
        super().save()

    class Meta:
        verbose_name = 'Фотографию'
        verbose_name_plural = 'Фотографии'
        ordering = ['-pk']
    
    


class banner_akcii(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название акции')
    image = models.ImageField(verbose_name='Главное изображение', upload_to='banner')
    short_description = models.TextField(verbose_name='Краткое описание', blank=True, null=True)
    content = RichTextUploadingField(verbose_name='Основной контент', blank=True, null=True)
    href = models.TextField(verbose_name="Ссылка на акцию", blank=True, null=True)
    picture_url = models.CharField(max_length=200, verbose_name='Расположение пути', blank=True, null=True) 

    def save(self, *args, **kwargs):
        self.picture_url = self.image.url
        super().save()

    class Meta:
        verbose_name = 'Банер'
        verbose_name_plural = 'Банеры'

    def __str__(self) -> str:
        return self.title
    
    


class Categories(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название категории')
    icon = models.ImageField(verbose_name='Иконка категории', upload_to='categoties_icons')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Родительская категория')
    describe = models.TextField(verbose_name="Краткое описание", null=True, blank=True)
    slug = models.SlugField()
    picture_url = models.CharField(max_length=200, verbose_name='Расположение пути', blank=True, null=True) 
    
    def save(self, *args, **kwargs):
        self.picture_url = self.icon.url
        super().save()  # saving image first

        # img = Image.open(self.icon.path)  # Open image using self

        # if (img.height != 75 or img.width != 450) and self.parent is not None:
        #     new_img = (450, 75)
        #     img.thumbnail(new_img)
        #     img.save(self.icon.path)
    
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
    description = RichTextUploadingField(verbose_name='Описание техники', blank=True, null=True)
    categories_id = models.ForeignKey('Categories', on_delete=models.CASCADE)
    slug = models.SlugField()
    picture_url = models.CharField(max_length=200, verbose_name='Расположение главного изображения', blank=True, null=True) 


    def save(self, *args, **kwargs):
        self.picture_url = self.main_image.url
        super().save()

    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техники'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('machineDetail', kwargs={'slug': self.slug})


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = RichTextUploadingField(verbose_name='Описание', blank=True, null=True)
    image = models.ImageField(verbose_name="Главная картинка новости", upload_to='news_image/')
    created_at = models.DateField(default=datetime.date.today, verbose_name='Дата создания')
    slug = models.SlugField()
    picture_url = models.CharField(max_length=200, verbose_name='Расположение пути', blank=True, null=True) 

    def save(self, *args, **kwargs):
        self.picture_url = self.image.url
        super().save()

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-pk']

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('postdetailview', kwargs={'slug': self.slug})


class OurPartners(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя партнера")
    image = models.ImageField(verbose_name="Изображение партнера", upload_to='partner_logos/')
    href = models.TextField(verbose_name="ссылка на партнера", blank=True, null=True)
    is_vip = models.BooleanField(verbose_name='VIP', default=False)
    rating = models.IntegerField(verbose_name="Рейтинг", default=0)

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

    def __str__(self) -> str:
        return self.name


class PageContent(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = RichTextUploadingField(verbose_name='Описание', blank=True, null=True)
    created_at = models.DateField(default=timezone.now, verbose_name='Дата создания')
    on_main_menu = models.BooleanField(verbose_name='Отображать в меню?',default=False)
    on_about_company = models.BooleanField(verbose_name='Отображать в разделе о компании?', default=False)
    href = models.CharField(max_length=200, verbose_name="Отдельная ссылка", blank=True, null=True)
    slug = models.SlugField()
     
    
    class Meta:
        verbose_name = 'Контент страницы'
        verbose_name_plural = 'Контенты страниц'
    

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('pagecontentdetail', kwargs={'slug': self.slug})


class ImportantInfo(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = RichTextUploadingField(verbose_name='Описание', blank=True, null=True)
    created_at = models.DateField(default=timezone.now, verbose_name='Дата создания')
    image = models.ImageField(verbose_name="Главная картинка", upload_to='important_info/')
    slug = models.SlugField()
    picture_url = models.CharField(max_length=200, verbose_name='Расположение главного изображения', blank=True, null=True)
    href = models.CharField(max_length=200, verbose_name="Отдельная ссылка", blank=True, null=True)

    def get_absolute_url(self):
        return reverse('important_info', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        self.picture_url = self.image.url
        super().save()

    class Meta:
        verbose_name = 'Важная информация'
        verbose_name_plural = 'Важная информация'

    def __str__(self) -> str:
        return self.title


class AkciiCategories(models.Model):
    title = models.CharField(verbose_name='Название категории акции', max_length=100)
    image = models.ImageField(verbose_name="Главная картинка", upload_to='akcii_category/')
    slug = models.SlugField()
    picture_url = models.CharField(max_length=200, verbose_name='Расположение главного изображения', blank=True, null=True) 

    def save(self, *args, **kwargs):
        self.picture_url = self.image.url
        super().save()
        
    class Meta:
        verbose_name = 'Категория акций'
        verbose_name_plural = 'Категории акций'

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('akciicategoriesdetail', kwargs={'slug': self.slug})

    def get_last_date(self):
        return Akcii.objects.filter(akciicategories=self.id).latest('created_at').created_at
        

class Akcii(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = RichTextUploadingField(verbose_name='Описание', blank=True, null=True)
    image = models.ImageField(verbose_name="Главная картинка акции", upload_to='akcii_image/')
    created_at = models.DateField(default=timezone.now, verbose_name='Дата создания')
    slug = models.SlugField()
    akciicategories = models.ForeignKey('AkciiCategories', on_delete=models.CASCADE)
    picture_url = models.CharField(max_length=200, verbose_name='Расположение главного изображения', blank=True, null=True) 

    def save(self, *args, **kwargs):
        self.picture_url = self.image.url
        super().save()

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
        ordering = ['-created_at', 'title']

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('akciidetail', kwargs={'slug': self.slug})


class Sertificates(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(verbose_name="Изображение", upload_to='sert/')

    class Meta:
        verbose_name = 'Сертификат (диплом)'
        verbose_name_plural = 'Сертификаты и дипломы'
        ordering = ['title']

    def __str__(self) -> str:
        return self.title


class Buklet(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(verbose_name="Изображение", upload_to='sert/')

    class Meta:
        verbose_name = 'Изображение буклета'
        verbose_name_plural = 'Изображения буклета'
        ordering = ['title']

    def __str__(self) -> str:
        return self.title


class Callback(models.Model):
    name = models.CharField(max_length=200, verbose_name="Обращение к Вам")
    telephon = models.CharField(max_length=100, verbose_name="Номер Вашего телефона", blank=True, null=True)
    is_obr = models.BooleanField(verbose_name="Обработан ли?", default=False)
    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    message = models.TextField(verbose_name="Текст сообщения", blank=True, null=True)
    

    def __str__(self) -> str:
        return "{} {}".format(self.name, self.telephon)

    class Meta:
        verbose_name = 'Обратный звонок'
        verbose_name_plural = 'Обратные звонки'
        ordering = ['is_obr']
