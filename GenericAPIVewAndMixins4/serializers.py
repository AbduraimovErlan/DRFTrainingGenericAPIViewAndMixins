from rest_framework import serializers
from GenericAPIVewAndMixins4.models import Book4



class SerializersBook4(serializers.ModelSerializer):
    class Meta:
        model = Book4
        fields = '__all__'