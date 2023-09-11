from django import template
from itertools import islice

from main.models import OurPartners, Post, banner_akcii, Categories, Photo

register = template.Library()


@register.simple_tag()
def get_photo():
    return Photo.objects.all()


@register.simple_tag()
def get_categories():
    return Categories.objects.filter(parent=None)


@register.simple_tag()
def get_banner_akcii():
    return banner_akcii.objects.all()


@register.simple_tag()
def get_ourpartners():
    ourpartners = OurPartners.objects.all()
    grouped_ourpartners = []
    while True:
        group = list(islice(ourpartners, 3))
        if len(group) == 0:
            break
        grouped_ourpartners.append(group)
        ourpartners = ourpartners[3::]
    return grouped_ourpartners

@register.simple_tag()
def get_news():
    posts = Post.objects.all()
    grouped_posts = []
    while True:
        # Возьмите 4 объекта из оставшихся объектов
        group = list(islice(posts, 4))
        # Если группа пустая, значит все объекты уже были добавлены

        if len(group) == 0:
            break
        grouped_posts.append(group)
        posts = posts[4::]
    return grouped_posts