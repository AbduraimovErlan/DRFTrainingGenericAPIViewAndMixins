from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from GenericAPIVewAndMixins6.models import Book6
from GenericAPIVewAndMixins6.serializers import SerializersBook6




class BookListCreateAPIView6(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Book6.objects.all()
    serializer_class = SerializersBook6


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookRetrieveUpdateDestroy6(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Book6.objects.all()
    serializer_class = SerializersBook6


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
