from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


@admin.register(models.PartnersCategory)
class PartnersCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'slug')
    exclude = ['picture_url']
    prepopulated_fields = {'slug': ('title',), }


@admin.register(models.Albom)
class AlbomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'picture', 'description', 'prewiew')
    list_display_links = ('id', 'name', 'date')
    search_fields = ('title', 'name')
    prepopulated_fields = {'slug': ('name',), }

    def prewiew(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="max-width: 70%;">')


@admin.register(models.OurPartners)
class OurPartnersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'prewiew',  'is_vip', 'rating', 'category_parners_id')
    list_display_links = ('id', 'name', 'prewiew',  'is_vip', 'rating', 'category_parners_id')
    search_fields = ('id', 'name',)

    def prewiew(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-width: 70%;">')

@admin.register(models.Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }


@admin.register(models.Machine)
class MachineAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), 'picture_url': ('main_image',),}


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'picture', 'albom_id', 'prewiew')
    list_display_links = ('id', 'prewiew')
    search_fields = ('albom_id',)

    def prewiew(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="max-width: 10%;">')


@admin.register(models.PageContent)
class PageContentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


@admin.register(models.ImportantInfo)
class ImportantInfoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


@admin.register(models.AkciiCategories)
class AkciiCategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


@admin.register(models.Akcii)
class AkciiAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(models.Photo, PhotoAdmin)
admin.site.register(models.banner_akcii)
admin.site.register(models.Buklet)
admin.site.register(models.Sertificates)

admin.site.register(models.Callback)