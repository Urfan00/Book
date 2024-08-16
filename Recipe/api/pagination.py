from rest_framework.pagination import PageNumberPagination


class SmallPageNumberPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'sayfa'


class LargePageNumberPagination(PageNumberPagination):
    page_size = 7
    page_query_param = 'num'


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000
