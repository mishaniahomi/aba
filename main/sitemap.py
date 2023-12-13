from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Post, Akcii, Albom, AkciiCategories, Categories, ImportantInfo, Machine, PageContent 


class PageContentSitemap(Sitemap):
    changefreq = 'weekly'  
    priority = 0.9  
  
    def items(self):  
        return PageContent.objects.all()  
      
    def lastmod(self, obj):  
        return obj.created_at 
    

class MachineSitemap(Sitemap):
    changefreq = 'weekly'  
    priority = 0.9  
  
    def items(self):  
        return Machine.objects.all()  
      
    # def lastmod(self, obj):  
    #     return obj.created_at
    

class ImportantInfoSitemap(Sitemap):
    changefreq = 'weekly'  
    priority = 0.9  
  
    def items(self):  
        return ImportantInfo.objects.all()  
      
    def lastmod(self, obj):  
        return obj.created_at 
    

class CategoriesSitemap(Sitemap):
    changefreq = 'weekly'  
    priority = 0.9  
  
    def items(self):  
        return Categories.objects.all()  


class AkciiCategoriesSitemap(Sitemap):
    changefreq = 'weekly'  
    priority = 0.9  
  
    def items(self):  
        return AkciiCategories.objects.all()  
      
    def lastmod(self, obj):  
        return obj.get_last_date() 
    

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
        return ['index', 'akcii', ]

    

    def location(self, item):
        return reverse(item)