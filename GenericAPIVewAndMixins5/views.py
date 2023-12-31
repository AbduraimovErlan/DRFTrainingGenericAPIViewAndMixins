from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from GenericAPIVewAndMixins5.models import Book5
from GenericAPIVewAndMixins5.serializers import SerializersBook5



class BookListCreateAPIView5(GenericAPIView, ListModelMixin, CreateModelMixin):
        queryset = Book5.objects.all()
        serializer_class = SerializersBook5


        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)

        def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)


class BookRetrieveUpdateDestroyAPIView5(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Book5.objects.all()
    serializer_class = SerializersBook5

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)