from django.shortcuts import render
from rest_framework import generics

from category.models import Category
from category.serializers import CategorySerializer


# Create your views here.


class CategoryTreeList(generics.ListAPIView):
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_class = CategorySerializer
