from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


@admin.register(models.Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }

@admin.register(models.Machine)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }

admin.site.register(models.Photo)
admin.site.register(models.OurPartners)
admin.site.register(models.banner_akcii)
