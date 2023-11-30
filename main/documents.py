from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import Post, ImportantInfo, Akcii, Albom, Photo, banner_akcii, Categories, Machine, PageContent, AkciiCategories


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