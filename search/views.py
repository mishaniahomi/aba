from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from django.db.models import Q



from main.serializers import PostSerializer, ImportantInfoSerializer, AkciiCategoriesSerializer, AkciiSerializer, AlbomSerializer, banner_akciiSerializer, CategoriesSerializer, MachineSerializer, PageContentSerializer

from main.models import Post, ImportantInfo, AkciiCategories, Akcii, Machine, Albom, banner_akcii, Categories, PageContent

class SearchPosts(APIView):
    def get(self, request, query):
        queryset = Post.objects.filter(Q(content__icontains=query) | Q(title__icontains=query))
        serializer_for_queryset = PostSerializer(
            instance=queryset,  # Передаём набор записей
            many=True  # Указываем, что на вход подаётся именно набор записей
        )
        return Response(serializer_for_queryset.data)


class SearchImportantInfoh(APIView):
    def get(self, request, query):
        queryset = ImportantInfo.objects.filter(Q(content__icontains=query) | Q(title__icontains=query))
        serializer_for_queryset = ImportantInfoSerializer(
            instance=queryset,  # Передаём набор записей
            many=True  # Указываем, что на вход подаётся именно набор записей
        )
        return Response(serializer_for_queryset.data)


class SearchAkciiCategories(APIView):
    def get(self, request, query):
        queryset = AkciiCategories.objects.filter(Q(title__icontains=query))
        serializer_for_queryset = AkciiCategoriesSerializer(
            instance=queryset,  # Передаём набор записей
            many=True  # Указываем, что на вход подаётся именно набор записей
        )
        return Response(serializer_for_queryset.data)


class SearchAkcii(APIView):
    def get(self, request, query):
        queryset = Akcii.objects.filter(Q(content__icontains=query) | Q(title__icontains=query))
        serializer_for_queryset = AkciiSerializer(
            instance=queryset,  # Передаём набор записей
            many=True  # Указываем, что на вход подаётся именно набор записей
        )
        return Response(serializer_for_queryset.data)


class SearchMachine(APIView):
    def get(self, request, query):
        queryset = Machine.objects.filter(Q(description__icontains=query) | Q(name__icontains=query))
        serializer_for_queryset = MachineSerializer(
            instance=queryset,  # Передаём набор записей
            many=True  # Указываем, что на вход подаётся именно набор записей
        )
        return Response(serializer_for_queryset.data)


class SearchAlbom(APIView):
    def get(self, request, query):
        queryset = banner_akcii.objects.filter(Q(short_description__icontains=query) | Q(content__icontains=query) | Q(title__icontains=query))
        serializer_for_queryset = banner_akciiSerializer(
            instance=queryset,  # Передаём набор записей
            many=True  # Указываем, что на вход подаётся именно набор записей
        )
        return Response(serializer_for_queryset.data)


class SearchCategories(APIView):
    def get(self, request, query):
        queryset = Categories.objects.filter(Q(name__icontains=query) | Q(describe__icontains=query))
        serializer_for_queryset = CategoriesSerializer(
            instance=queryset,  # Передаём набор записей
            many=True  # Указываем, что на вход подаётся именно набор записей
        )
        return Response(serializer_for_queryset.data)

class SearchBannerAakcii(APIView):
    def get(self, request, query):
        queryset = Albom.objects.filter(Q(description__icontains=query))
        serializer_for_queryset = AlbomSerializer(
            instance=queryset,  # Передаём набор записей
            many=True  # Указываем, что на вход подаётся именно набор записей
        )
        return Response(serializer_for_queryset.data)


class SearchPageContent(APIView):
    def get(self, request, query):
        queryset = PageContent.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        serializer_for_queryset = PageContentSerializer(
            instance=queryset,  # Передаём набор записей
            many=True  # Указываем, что на вход подаётся именно набор записей
        )
        return Response(serializer_for_queryset.data)

def results(request):
    search_field = request.GET.getlist('search_field')
    if search_field:
        query = search_field[0]
    else:
        query = ""
    return render(request, 'search/results.html', context={'query': query}) 