from django import template
from itertools import islice
import math
from main.models import OurPartners, Post, banner_akcii, Categories, Photo, Albom, Machine

register = template.Library()


@register.simple_tag()
def get_photoes(albom_id):
    return Photo.objects.filter(albom_id=albom_id)

@register.simple_tag()
def get_machine(catgories_id):
    machine = Machine.objects.filter(categories_id=catgories_id)
    group_machine = []
    while True:
        group = list(islice(machine, 4))
        if len(group) == 0:
            break
        group_machine.append(group)
        machine = machine[3::]

    return group_machine

@register.simple_tag()
def get_alboms():
    alboms = Albom.objects.all()
    grouped_alboms = []
    while True:
        group = list(islice(alboms, 4))
        if len(group) == 0:
            break
        grouped_alboms.append(group)
        alboms = alboms[4::]


    return grouped_alboms


@register.simple_tag()
def get_categories():
    categories = Categories.objects.filter(parent=None)
    size = math.ceil(len(categories)/3)
    grouped_categories = []
    while True:
        group = list(islice(categories, size))
        if len(group) == 0:
            break
        grouped_categories.append(group)
        categories = categories[size::]
    return grouped_categories


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