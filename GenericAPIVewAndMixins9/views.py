from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from GenericAPIVewAndMixins9.models import Book9
from GenericAPIVewAndMixins9.serializers import SerializersBook9


class BookListCreateAPIView9(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Book9.objects.all()
    serializer_class = SerializersBook9

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookRetrieveUpdateDestroy9(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Book9.objects.all()
    serializer_class = SerializersBook9


    def get(self, reqeust, *args, **kwargs):
        return self.retrieve(reqeust, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)