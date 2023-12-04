from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Post, Akcii, Albom  #AkciiCategories, banner_akcii, Categories, ImportantInfo, Machine, PageContent 


class AlbomSitemap(Sitemap):
    changefreq = 'weekly'  
    priority = 0.9  
  
    def items(self):  
        return Albom.objects.all()  
      
    def lastmod(self, obj):  
        return obj.date 


class AkciiSitemap(Sitemap):  
    changefreq = 'weekly'  
    priority = 0.9  
  
    def items(self):  
        return Akcii.objects.all()  
      
    def lastmod(self, obj):  
        return obj.created_at 
  

class PostSitemap(Sitemap):  
    changefreq = 'weekly'  
    priority = 0.9  
  
    def items(self):  
        return Post.objects.all()  
      
    def lastmod(self, obj):  
        return obj.created_at
    

class StaticSitemap(Sitemap):
    """
    Карта-сайта для статичных страниц
    """

    def items(self):
        return ['index']

    

    def location(self, item):
        return reverse(item)