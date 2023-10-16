from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer

# Create your views here.


class ProductCategoryFiltering(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            category = self.request.GET.get('category')
            min_price = self.request.GET.get('min_price')
            max_price = self.request.GET.get('max_price')
            if min_price and max_price is not None:
                filtered_products = Product.objects.filter(category=category, price__gte=min_price, price__lte=max_price)
            else:
                filtered_products = Product.objects.filter(category=category)
            serialized_data = self.get_serializer(filtered_products, many=True).data
            return Response(serialized_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self, *args, **kwargs):
        product_uuid = self.request.GET.get('uuid')
        queryset = Product.objects.filter(article_uuid=product_uuid)
        return queryset



