from django.urls import path

from .views import SearchPosts, results, SearchImportantInfoh

urlpatterns = [
    path('posts/<str:query>/', SearchPosts.as_view()),
    path('importantinfo/<str:query>/', SearchImportantInfoh.as_view()),
    path('results/', results, name='search_result' )

]
