from django.shortcuts import render
from rest_framework import viewsets

from .models import Buku, Penulis
from .serializers import BukuSerializers, PenulisSerializers
# Create your views here.


class BukuViewSet(viewsets.ModelViewSet):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializers


class PenulisViewSet(viewsets.ModelViewSet):
    queryset = Penulis.objects.all()
    serializer_class = PenulisSerializers
