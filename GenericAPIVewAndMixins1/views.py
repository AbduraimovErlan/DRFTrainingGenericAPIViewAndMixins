from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from GenericAPIVewAndMixins1.models import Book1
from GenericAPIVewAndMixins1.serializers import SerializersBook1





class BookListCreateView1(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Book1.objects.all()
    serializer_class = SerializersBook1

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BookRetrieveUpdateDestroyView1(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Book1.objects.all()
    serializer_class = SerializersBook1

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)