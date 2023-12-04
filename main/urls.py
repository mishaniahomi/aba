from django.urls import path
from .views import index, PostDetailView, akcii, categoryView, AlbomDetail, \
    MachineDetail, PageContentDetailView, AkciiCategoriesDetail, AkciiDetail, SertificatesView, BukletView, ImportantInfoDetailView


urlpatterns = [
    path('news/<slug:slug>/', PostDetailView.as_view(), name='postdetailview'),
    path('akciicategories', akcii, name='akcii'),
    path('category/<slug:slug>', categoryView, name='category'),
    path('', index, name='index'),
    path('albom/<slug:slug>', AlbomDetail.as_view(), name='albomDetail'),
    path('category/machine/<slug:slug>', MachineDetail.as_view(), name='machineDetail'),
    path('content/<slug:slug>', PageContentDetailView.as_view(), name='pagecontentdetail'),
    path('akciicategories/<slug:slug>', AkciiCategoriesDetail.as_view(), name='akciicategoriesdetail'),
    path('akcii/<slug:slug>', AkciiDetail.as_view(), name='akciidetail'),
    path('sert', SertificatesView, name='sert'),
    path('buklet', BukletView, name='buklet'),
    path('important_info/<slug:slug>', ImportantInfoDetailView.as_view(), name='important_info')
] 
