# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.decorators.csrf import csrf_exempt

from .models import OurPartners, Post, Categories, Albom, Machine, PageContent, AkciiCategories, Akcii, Sertificates, Buklet, ImportantInfo
from .forms import CallBackForm

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    slug_field = 'slug'


class ImportantInfoDetailView(DetailView):
    model = ImportantInfo
    context_object_name = 'ImportantInfo'
    slug_field = 'slug'


class PageContentDetailView(DetailView):
    model = PageContent
    context_object_name = 'content'
    slug_field = 'slug'


@csrf_exempt
def index(request):
    if request.method == 'POST':
        form = CallBackForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'main/index.html')


def akcii(request):
    return render(request, 'main/akcii.html')


def categoryView(request, slug):
    category = Categories.objects.get(slug=slug)
    child_categories = Categories.objects.filter(parent=category)
    return render(request, 'main/category.html', {'category': category, 'child_categories': child_categories})


class AlbomDetail(DetailView):
    model = Albom


class MachineDetail(DetailView):
    model = Machine


class AkciiCategoriesDetail(DetailView):
    model = AkciiCategories


class AkciiDetail(DetailView):
    model = Akcii


def SertificatesView(request):
    sertificaties = Sertificates.objects.all()
    return render(request, 'main/SertificatesView.html', context={'sertificaties': sertificaties})


def BukletView(request):
    buklets = Buklet.objects.all()
    return render(request, 'main/buklet.html', context={'sertificaties': buklets})


def yandex(request):
    return render(request, 'yandex_0851d15aa1667e58.html')


def OurPartnersView(request):
    ourpartners = OurPartners.objects.all().order_by('-rating')
    return  render(request, 'main/our_partners.html', context={'ourpartners': ourpartners})
