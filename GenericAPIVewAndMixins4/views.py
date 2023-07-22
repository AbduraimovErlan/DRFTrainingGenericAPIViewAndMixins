from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from GenericAPIVewAndMixins4.models import Book4
from GenericAPIVewAndMixins4.serializers import SerializersBook4



class BookListCreateAPIView4(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Book4.objects.all()
    serializer_class = SerializersBook4

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BookRetrieveUpdateDestroyAPIView4(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Book4.objects.all()
    serializer_class = SerializersBook4


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)