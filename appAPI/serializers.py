from rest_framework import serializers

from .models import Buku, Penulis


class BukuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Buku
        fields = '__all__'


class PenulisSerializers(serializers.ModelSerializer):
    class Meta:
        model = Penulis
        fields = '__all__'
