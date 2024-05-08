from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status

class CustomPagination(PageNumberPagination):
    """
    Custom Pagination class for API views

    Here, page_size = 10, page_size_query_param = 'page_size', max_page_size = 100
    """
    page_size = 7
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'success': True,
            'status': status.HTTP_200_OK,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'results': data
        })