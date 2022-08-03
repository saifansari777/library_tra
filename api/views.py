from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Book
from .serializers import BookSerializer


class BookList(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

