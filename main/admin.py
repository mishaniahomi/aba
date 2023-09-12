from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


@admin.register(models.Albom)
class AlbomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'picture', 'description', 'prewiew')
    list_display_links = ('id', 'name', 'date')
    search_fields = ('title', 'name')
    prepopulated_fields = {'slug': ('name',), }

    def prewiew(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="max-width: 70%;">')


@admin.register(models.Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }


@admin.register(models.Machine)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'picture', 'albom_id', 'prewiew')
    list_display_links = ('id', 'prewiew')
    search_fields = ('albom_id',)

    def prewiew(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="max-width: 10%;">')

admin.site.register(models.Photo, PhotoAdmin)
admin.site.register(models.OurPartners)
admin.site.register(models.banner_akcii)
