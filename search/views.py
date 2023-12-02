import abc
from django.shortcuts import render
from django.http import HttpResponse
from elasticsearch_dsl import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView


from main.documents import PostDocument, ImportantInfoDocument, AkciiCategoriesDocument, Banner_akciiDocument, CategoriesDocument, AkciiDocument, AlbomDocument, MachineDocument, PageContentDocument
from main.serializers import PostSerializer, ImportantInfoSerializer, AkciiCategoriesSerializer, AkciiSerializer, AlbomSerializer, banner_akciiSerializer, CategoriesSerializer, MachineSerializer, PageContentSerializer


class PaginatedElasticSearchAPIView(APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """This method should be overridden
        and return a Q() expression."""

    def get(self, request, query):
        try:
            q = self.generate_q_expression(query)
            search = self.document_class.search().query(q)
            response = search.execute()

            print(f'Found {response.hits.total.value} hit(s) for query: "{query}"')

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)


class SearchPageContent(PaginatedElasticSearchAPIView):
    serializer_class = PageContentSerializer
    document_class = PageContentDocument

    def generate_q_expression(self, query):
        return Q(
                    'multi_match', query=query,
                    fields=[
                    'title',
                    'content',
                ], fuzziness='auto')
    

class SearchMachine(PaginatedElasticSearchAPIView):
    serializer_class = MachineSerializer
    document_class = MachineDocument

    def generate_q_expression(self, query):
        return Q(
                    'multi_match', query=query,
                    fields=[
                    'name',
                    'preview_description',
                    'description',
                ], fuzziness='auto')
    
    
class SearchAlbom(PaginatedElasticSearchAPIView):
    serializer_class = AlbomSerializer
    document_class = AlbomDocument

    def generate_q_expression(self, query):
        return Q(
                    'multi_match', query=query,
                    fields=[
                    'name',
                    'description',
                ], fuzziness='auto')
    

class SearchAkcii(PaginatedElasticSearchAPIView):
    serializer_class = AkciiSerializer
    document_class = AkciiDocument

    def generate_q_expression(self, query):
        return Q(
                    'multi_match', query=query,
                    fields=[
                    'title',
                    'content',
                ], fuzziness='auto')
    

class SearchCategories(PaginatedElasticSearchAPIView):
    serializer_class = CategoriesSerializer
    document_class = CategoriesDocument

    def generate_q_expression(self, query):
        return Q(
                    'multi_match', query=query,
                    fields=[
                    'name',
                    'describe',
                ], fuzziness='auto')
    

class SearchBannerAakcii(PaginatedElasticSearchAPIView):
    serializer_class = banner_akciiSerializer
    document_class = Banner_akciiDocument

    def generate_q_expression(self, query):
        return Q(
                    'multi_match', query=query,
                    fields=[
                    'title',
                    'short_description',
                    'content',
                ], fuzziness='auto')
    

class SearchAkciiCategories(PaginatedElasticSearchAPIView):
    serializer_class = AkciiCategoriesSerializer
    document_class = AkciiCategoriesDocument

    def generate_q_expression(self, query):
        return Q(
                    'multi_match', query=query,
                    fields=[
                    'title',
                ], fuzziness='auto')
    

class SearchImportantInfoh(PaginatedElasticSearchAPIView):
    serializer_class = ImportantInfoSerializer
    document_class = ImportantInfoDocument

    def generate_q_expression(self, query):
        return Q(
                    'multi_match', query=query,
                    fields=[
                    'id',
                    'title',
                    'content',
                    'slug'
                ], fuzziness='auto')
    

class SearchPosts(PaginatedElasticSearchAPIView):
    serializer_class = PostSerializer
    document_class = PostDocument

    def generate_q_expression(self, query):
        return Q(
                    'multi_match', query=query,
                    fields=[
                    'id',
                    'title',
                    'content',
                    'slug'
                ], fuzziness='auto')
    

def results(request):
    search_field = request.GET.getlist('search_field')
    if search_field:
        query = search_field[0]
    else:
        query = ""
    return render(request, 'search/results.html', context={'query': query}) 