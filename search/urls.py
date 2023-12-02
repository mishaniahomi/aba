from django.urls import path

from .views import SearchPosts, results, SearchImportantInfoh, SearchAkcii, SearchAkciiCategories, SearchAlbom, SearchBannerAakcii, SearchCategories, SearchMachine, SearchPageContent


urlpatterns = [
    path('posts/<str:query>/', SearchPosts.as_view()),
    path('importantinfo/<str:query>/', SearchImportantInfoh.as_view()),
    path('machine/<str:query>/', SearchMachine.as_view()),
    path('akcii/<str:query>/', SearchAkcii.as_view()),
    path('akciicategories/<str:query>/', SearchAkciiCategories.as_view()),
    path('albom/<str:query>/', SearchAlbom.as_view()),
    path('banneraakcii/<str:query>/', SearchBannerAakcii.as_view()),
    path('categories/<str:query>/', SearchCategories.as_view()),
    path('pagecontent/<str:query>/', SearchPageContent.as_view()),
    path('results/', results, name='search_result' )
]
