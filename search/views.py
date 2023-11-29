import abc
from django.shortcuts import render
from django.http import HttpResponse
from elasticsearch_dsl import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView


from main.documents import PostDocument
from main.serializers import PostSerializer


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