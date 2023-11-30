from rest_framework import serializers

from .models import Post, ImportantInfo, Akcii, Albom, Photo, banner_akcii, Categories, Machine, PageContent, AkciiCategories


class AkciiCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AkciiCategories
        fields = '_all__'


class PageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContent
        fields = '_all__'


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '_all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '_all__'


class banner_akciiSerializer(serializers.ModelSerializer):
    class Meta:
        model = banner_akcii
        fields = '_all__'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '_all__'


class AlbomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = '_all__'


class AkciiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Akcii
        fields = '_all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =  '__all__' #('id', 'content', 'title', 'slug', 'created_at')


class ImportantInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportantInfo
        fields = '__all__'
