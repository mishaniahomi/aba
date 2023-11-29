from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =  '__all__' #('id', 'content', 'title', 'slug', 'created_at')