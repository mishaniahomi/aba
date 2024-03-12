from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils import timezone
import datetime


class Albom(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название альбома')
    date = models.DateField(verbose_name='Дата создания')
    picture = models.ImageField(verbose_name='Обожка', upload_to='albom')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField()
    picture_url = models.CharField(max_length=200, verbose_name='Расположение пути', blank=True, null=True)
    visible = models.BooleanField(verbose_name='Видно ли в галереи', default=True)

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
    created_at = models.DateField(default=datetime.date.today, verbose_name='Дата создания')

    def save(self, *args, **kwargs):
        self.picture_url = self.image.url
        super().save()

    class Meta:
        verbose_name = 'Банер'
        verbose_name_plural = 'Банеры'
        ordering = ['-created_at', '-pk']

    def __str__(self) -> str:
        return self.title
    
    


class Categories(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название категории')
    icon = models.ImageField(verbose_name='Иконка категории', upload_to='categoties_icons')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Родительская категория')
    describe = models.TextField(verbose_name="Краткое описание", null=True, blank=True)
    slug = models.SlugField()
    picture_url = models.CharField(max_length=200, verbose_name='Расположение пути', blank=True, null=True)
    created_at = models.DateField(default=datetime.date.today, verbose_name='Дата создания')
    
    def save(self, *args, **kwargs):
        self.picture_url = self.icon.url
        super().save()  # saving image first
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-created_at', '-pk']

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
    created_at = models.DateField(default=datetime.date.today, verbose_name='Дата создания')

    def save(self, *args, **kwargs):
        self.picture_url = self.main_image.url
        super().save()

    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техники'
        ordering = ['-created_at', '-pk']

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
        ordering = ['-created_at', '-pk']

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
    category_parners_id = models.ForeignKey('PartnersCategory', on_delete=models.SET_NULL, verbose_name="Категория партнёра", blank=True, null=True)

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
        ordering = ['rating', '-pk']

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
        ordering = ['-created_at', '-pk']
    

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
        ordering = ['-created_at', '-pk']
    def __str__(self) -> str:
        return self.title


class AkciiCategories(models.Model):
    title = models.CharField(verbose_name='Название категории акции', max_length=100)
    image = models.ImageField(verbose_name="Главная картинка", upload_to='akcii_category/')
    slug = models.SlugField()
    picture_url = models.CharField(max_length=200, verbose_name='Расположение главного изображения', blank=True, null=True)
    created_at = models.DateField(default=datetime.date.today, verbose_name='Дата создания')

    def save(self, *args, **kwargs):
        self.picture_url = self.image.url
        super().save()
        
    class Meta:
        verbose_name = 'Категория акций'
        verbose_name_plural = 'Категории акций'
        ordering = ['-created_at']

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
    created_at = models.DateField(default=datetime.date.today, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Сертификат (диплом)'
        verbose_name_plural = 'Сертификаты и дипломы'
        ordering = ['-created_at', '-pk']

    def __str__(self) -> str:
        return self.title


class Buklet(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(verbose_name="Изображение", upload_to='sert/')
    created_at = models.DateField(default=datetime.date.today, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Изображение буклета'
        verbose_name_plural = 'Изображения буклета'
        ordering = ['-created_at', 'title']

    def __str__(self) -> str:
        return self.title


class Callback(models.Model):
    name = models.CharField(max_length=200, verbose_name="Обращение к Вам")
    telephon = models.CharField(max_length=100, verbose_name="Номер Вашего телефона", blank=True, null=True)
    is_obr = models.BooleanField(verbose_name="Обработан ли?", default=False)
    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    message = models.TextField(verbose_name="Текст сообщения", blank=True, null=True)
    created_at = models.DateField(default=datetime.date.today, verbose_name='Дата создания')
    

    def __str__(self) -> str:
        return "{} {}".format(self.name, self.telephon)

    class Meta:
        verbose_name = 'Обратный звонок'
        verbose_name_plural = 'Обратные звонки'
        ordering = ['created_at', 'is_obr']


class PartnersCategory(models.Model):
    name = models.CharField(max_length=252, verbose_name="Название категории партнёров")
    created_at = models.DateField(default=datetime.date.today, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория партнёров'
        verbose_name_plural = 'Категории партнёров'
        ordering = ['-created_at', '-pk']


class Albom_important_info(models.Model):
    albom_id = models.ForeignKey('Albom', on_delete=models.CASCADE, verbose_name='Альбом')
    important_info = models.ForeignKey('ImportantInfo', on_delete=models.CASCADE, verbose_name='Важная информация')

    def __str__(self):
        return "{} - {}".format(self.albom_id, self.important_info)

    class Meta:
        verbose_name = 'Связи альбомов и важной информации'
        verbose_name_plural = 'Связь альбома и важной информации'


class Albom_Akcii(models.Model):
    albom_id = models.ForeignKey('Albom', on_delete=models.CASCADE, verbose_name='Альбом')
    Akcii_id = models.ForeignKey('Akcii', on_delete=models.CASCADE, verbose_name='Акция', unique=True)

    def __str__(self):
        return "{} - {}".format(self.albom_id, self.Akcii_id)

    class Meta:
        verbose_name = 'Связи альбомов и акций'
        verbose_name_plural = 'Связь альбома и акции'


class Albom_Content(models.Model):
    albom_id = models.ForeignKey('Albom', on_delete=models.CASCADE, verbose_name='Альбом')
    pagecontent_id = models.ForeignKey('PageContent', on_delete=models.CASCADE, verbose_name='Контент страницы', unique=True)

    def __str__(self):
        return "{} - {}".format(self.albom_id, self.pagecontent_id)

    class Meta:
        verbose_name = 'Связи альбомов и контентов страниц'
        verbose_name_plural = 'Связь альбома и контента страницы'


class Albom_Post(models.Model):
    albom_id = models.ForeignKey('Albom', on_delete=models.CASCADE, verbose_name='Альбом')
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name='Новость', unique=True)

    def __str__(self):
        return "{} - {}".format(self.albom_id, self.post_id)

    class Meta:
        verbose_name = 'Связи альбомов и нововстей'
        verbose_name_plural = 'Связь альбома и новости'


class Albom_Machine(models.Model):
    albom_id = models.ForeignKey('Albom', on_delete=models.CASCADE, verbose_name='Альбом')
    machine_id = models.ForeignKey('Machine', on_delete=models.CASCADE, verbose_name='Новость', unique=True)

    def __str__(self):
        return "{} - {}".format(self.albom_id, self.machine_id)

    class Meta:
        verbose_name = 'Связи альбомов и техники'
        verbose_name_plural = 'Связь альбома и техники'