from django.urls import path

from .views import SearchPosts

urlpatterns = [
    path('posts/<str:query>/', SearchPosts.as_view()),

]
