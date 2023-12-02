from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import Post, ImportantInfo, Akcii, Albom, banner_akcii, Categories, Machine, PageContent, AkciiCategories


@registry.register_document
class AlbomDocument(Document):

    class Index:
        name = 'albom'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }
    
    class Django:
        model = Albom
        fields = [
            'name',
            'date',
            'description',
            'slug',
            'picture_url',
        ]

@registry.register_document
class PostDocument(Document):
    ps = fields.IntegerField()
    content = fields.TextField()
    picture_url = fields.TextField()
    class Index:
        name = 'posts'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }
    
    class Django:
        model = Post
        fields = [
            'title',
            'created_at',
            'slug',
        ]


@registry.register_document
class ImportantInfoDocument(Document):
    ps = fields.IntegerField()
    content = fields.TextField()
    picture_url = fields.TextField()
    class Index:
        name = 'important_info'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }
    
    class Django:
        model = ImportantInfo
        fields = [
            'title',
            'created_at',
            'slug',
        ]


@registry.register_document
class AkciiDocument(Document):
    ps = fields.IntegerField()
    content = fields.TextField()
    picture_url = fields.TextField()
    class Index:
        name = 'akcii'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }
    
    class Django:
        model = Akcii
        fields = [
            'title',
            'created_at',
            'slug',
        ]


@registry.register_document
class Banner_akciiDocument(Document):
    ps = fields.IntegerField()
    content = fields.TextField()

    class Index:
        name = 'bannerakcii'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }
    
    class Django:
        model = banner_akcii
        fields = [
            'title',
            'picture_url',
            'short_description',
            'href'
        ]


@registry.register_document
class CategoriesDocument(Document):
    ps = fields.IntegerField()
    content = fields.TextField()

    class Index:
        name = 'categories'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }
    
    class Django:
        model = Categories
        fields = [
            'name',
            'picture_url',
            'describe',
            'slug'
        ]


@registry.register_document
class MachineDocument(Document):
    ps = fields.IntegerField()
    preview_description = fields.TextField()
    description = fields.TextField()

    class Index:
        name = 'machine'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }
    
    class Django:
        model = Machine
        fields = [
            'name',
            'slug',
            'picture_url'
        ]


@registry.register_document
class PageContentDocument(Document):
    ps = fields.IntegerField()
    content = fields.TextField()

    class Index:
        name = 'pagecontent'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }
    
    class Django:
        model = PageContent
        fields = [
            'title',
            'created_at',
            'on_main_menu',
            'href',
            'slug'
        ]


@registry.register_document
class AkciiCategoriesDocument(Document):
    ps = fields.IntegerField()

    class Index:
        name = 'akciicategories'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }
    
    class Django:
        model = AkciiCategories
        fields = [
            'title',
            'slug',
            'picture_url'
        ]