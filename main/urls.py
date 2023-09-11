from django.urls import path
from .views import index, PostDetailView, zapchasti, servis, akcii, finansovye_instrumenty, categoryView


urlpatterns = [
    path('news/<slug:slug>/', PostDetailView.as_view(), name='postdetailview'),
    path('zapchasti', zapchasti, name='zapchasti'),
    path('servis', servis, name='servis'),
    path('akcii', akcii, name='akcii'),
    path('category/<slug:slug>', categoryView, name='category'),
    path('finansovye_instrumenty', finansovye_instrumenty, name='finansovye_instrumenty'),
    path('', index, name='index'),

] 
