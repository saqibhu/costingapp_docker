from django.shortcuts import render
from rest_framework import viewsets, generics

from .models import TblProduct
from .serializers import TblProductSerializer


class ListTblProduct(generics.ListCreateAPIView):
    queryset = TblProduct.objects.all()
    serializer_class = TblProductSerializer


class DetailTblProduct(generics.RetrieveUpdateAPIView):
    queryset = TblProduct.objects.all()
    serializer_class = TblProductSerializer

# Change list view to be list only i.e. read only
# Create a new impression against an existing product therefore under detail view
# still need to update the detail view
