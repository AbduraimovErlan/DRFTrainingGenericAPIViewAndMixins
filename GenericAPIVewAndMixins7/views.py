from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from GenericAPIVewAndMixins7.models import Book7
from GenericAPIVewAndMixins7.serializers import SerializersBook7



class BookListCreateAPIView7(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Book7.objects.all()
    serializer_class = SerializersBook7


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookRetrieveUpdateDestroy7(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Book7.objects.all()
    serializer_class = SerializersBook7

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)