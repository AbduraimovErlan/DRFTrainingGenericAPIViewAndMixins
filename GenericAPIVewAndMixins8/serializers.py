from rest_framework import serializers
from GenericAPIVewAndMixins8.models import Book8



class SerializersBook8(serializers.ModelSerializer):
    class Meta:
        model = Book8
        fields = '__all__'