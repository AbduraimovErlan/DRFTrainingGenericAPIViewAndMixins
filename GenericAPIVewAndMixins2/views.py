from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from GenericAPIVewAndMixins2.models import Book2
from GenericAPIVewAndMixins2.serializers import SerializersBook2



class BookListCreateAPIView2(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Book2.objects.all()
    serializer_class = SerializersBook2


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BookRetrieveUpdateDestroyAPIView2(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Book2.objects.all()
    serializer_class = SerializersBook2

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, reqeust, *args, **kwargs):
        return self.destroy(reqeust, *args, **kwargs)



