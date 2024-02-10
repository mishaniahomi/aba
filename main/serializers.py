from rest_framework import serializers

from .models import Post, ImportantInfo, Akcii, Albom, banner_akcii, Categories, Machine, PageContent, AkciiCategories


class AkciiCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AkciiCategories
        fields = ('id', 'title', 'slug', 'picture_url')


class PageContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PageContent
        fields = "__all__"


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ('id', 'name', 'description', 'slug', 'picture_url')



class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'name', 'describe', 'slug', 'picture_url')



class banner_akciiSerializer(serializers.ModelSerializer):
    class Meta:
        model = banner_akcii
        fields = ('id', 'title', 'short_description', 'content', 'href', 'picture_url')


class AlbomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Albom
        fields = ('id', 'description', 'slug', 'picture_url')


class AkciiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Akcii
        fields = ('id', 'title', 'slug', 'picture_url', 'content')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields =  ('id', 'content', 'title', 'slug', 'picture_url')


class ImportantInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImportantInfo
        fields =  ('id', 'content', 'title', 'slug', 'picture_url')
