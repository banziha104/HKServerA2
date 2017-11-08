
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class DataPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'link':{
                'next':None,
                'previous':None
            },
            'count': self.page.paginator.count,
            'results':data
        })