from core.models import Book

from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', "author",'description', "status", "created_at", "updated_at")


