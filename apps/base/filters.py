# Third Party Stuff
from rest_framework.filters import SearchFilter
from rest_framework import filters


class SearchWithWhitespaceFilter(SearchFilter):
    def get_search_terms(self, request):
        return [request.query_params.get("title", "").lstrip().rstrip()]