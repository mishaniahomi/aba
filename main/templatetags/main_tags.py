from django import template
from itertools import islice
import math
import datetime

from main.models import Albom_Machine, Albom_Post, Albom_important_info, Albom_Content, Albom_Akcii, OurPartners, Post, banner_akcii, Categories, Photo, Albom, Machine, PageContent, ImportantInfo, AkciiCategories, Akcii, PartnersCategory
from main.forms import CallBackForm

register = template.Library()


@register.simple_tag()
def get_photoes(albom_id):
    return Photo.objects.filter(albom_id=albom_id)

@register.simple_tag()
def get_machine(catgories_id):
    machine = Machine.objects.filter(categories_id=catgories_id)
    group_machine = []
    while True:
        group = list(islice(machine, 3))
        if len(group) == 0:
            break
        group_machine.append(group)
        machine = machine[3::]

    return group_machine

@register.simple_tag()
def get_alboms():
    alboms = Albom.objects.filter(visible=True)
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
    ourpartners = OurPartners.objects.filter(is_vip=True).order_by('rating')
    grouped_ourpartners = []
    while True:
        group = list(islice(ourpartners, 6))        
        if len(group) == 0:
            break
        grouped_ourpartners.append(group)
        ourpartners = ourpartners[6::]
    return grouped_ourpartners


@register.simple_tag()
def get_news():
    posts = Post.objects.filter(created_at__lte=datetime.date.today())
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


@register.simple_tag()
def get_contentpagies():
    objects = PageContent.objects.filter(on_main_menu=False)
    return objects


@register.simple_tag()
def get_contentpagies_on_board():
    objects = PageContent.objects.filter(on_main_menu=True)
    return objects


@register.simple_tag()
def get_important_info():
    posts = ImportantInfo.objects.all().order_by('-pk')
    grouped_posts = []
    while True:
        group = list(islice(posts, 4))
        if len(group) == 0:
            break
        grouped_posts.append(group)
        posts = posts[4::]
    return grouped_posts

@register.simple_tag()
def get_child_categories(category_id):
    return Categories.objects.filter(parent_id=category_id)

@register.simple_tag()
def get_AkciiCategories():
    return AkciiCategories.objects.all()


@register.simple_tag()
def get_Akcii(category_id):
    akcii = Akcii.objects.filter(akciicategories=category_id)
    group_akcii = []
    while True:
        group = list(islice(akcii, 3))
        if len(group) == 0:
            break
        group_akcii.append(group)
        akcii = akcii[3::]
    return group_akcii

@register.simple_tag()
def get_callback_form():
    return CallBackForm


@register.simple_tag()
def get_category_of_partners():
    return PartnersCategory.objects.all()


@register.simple_tag()
def get_partners_by_category(category_parners_id):
    return OurPartners.objects.filter(category_parners_id=category_parners_id)


@register.simple_tag()
def get_albom_of_akcii(akcii_id):
    return Albom_Akcii.objects.filter(Akcii_id=akcii_id)


@register.simple_tag()
def get_albom_of_important_info(important_info_id):
    return Albom_important_info.objects.filter(important_info=important_info_id)


@register.simple_tag()
def get_albom_of_content(pagecontent_id):
    return Albom_Content.objects.filter(pagecontent_id=pagecontent_id)


@register.simple_tag()
def get_albom_of_post(post_id):
    return Albom_Post.objects.filter(post_id=post_id)


@register.simple_tag()
def get_albom_of_machine(machine_id):
    return Albom_Machine.objects.filter(machine_id=machine_id)