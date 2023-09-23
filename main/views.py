# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import DetailView

from .models import Post, Categories, Albom, Machine, PageContent


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    slug_field = 'slug'


class PageContentDetailView(DetailView):
    model = PageContent
    context_object_name = 'content'
    slug_field = 'slug'


def index(request):
    return render(request, 'main/index.html')


def zapchasti(request):
    return render(request, 'main/zapchasti.html')


def servis(request):
    return render(request, 'main/servis.html')


def akcii(request):
    return render(request, 'main/akcii.html')


def finansovye_instrumenty(request):
    return render(request, 'main/finansovye-instrumenty.html')


def categoryView(request, slug):
    category = Categories.objects.get(slug=slug)
    child_categories = Categories.objects.filter(parent=category)
    return render(request, 'main/category.html', {'category': category, 'child_categories': child_categories })


class AlbomDetail(DetailView):
    model = Albom


class MachineDetail(DetailView):
    model = Machine
