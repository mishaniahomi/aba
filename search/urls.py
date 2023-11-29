from django.urls import path

from .views import SearchPosts, results

urlpatterns = [
    path('posts/<str:query>/', SearchPosts.as_view()),
    path('results/', results, name='search_result' )

]
