from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from GenericAPIVewAndMixins8.serializers import SerializersBook8
from GenericAPIVewAndMixins8.models import Book8


class BookListCreateAPIView8(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Book8.objects.all()
    serializer_class = SerializersBook8


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookRetrieveUpdateDestroy(GenericAPIView, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = Book8.objects.all()
    serializer_class = SerializersBook8


    def get(self, reqeust, *args, **kwargs):
        return self.retrieve(reqeust, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)