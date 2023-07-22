from rest_framework import serializers
from GenericAPIVewAndMixins7.models import Book7



class SerializersBook7(serializers.ModelSerializer):
    class Meta:
        model = Book7
        fields = '__all__'