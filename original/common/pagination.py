# -*- coding: utf-8 -*-
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ViewPagination(PageNumberPagination):
    page_query_param = "page"
    page_size_query_param = "limit"
    page_size = 200
    max_page_size = 200

    def get_paginated_response(self, data):
        return Response({
            'meta': {
                'total': self.page.paginator.count,
                'current_count': len(data),
                'page': self.page.number,
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
            },
            'data': data
        })
