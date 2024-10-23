from itertools import product

from django.shortcuts import render
from .models import Product
from rest_framework import viewsets, generics, filters
from .serializers import ProductSerializers
# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset =Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id','name']
class ProductdetailViewSet(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'id'