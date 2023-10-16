from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cart.models import Cart
from cart.serializers import CartSerializer
from product.models import Product
from product_list.models import ProductList


# Create your views here.


class CartList(generics.ListAPIView):
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user_id=user)


class CartAddProducts(generics.CreateAPIView):
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')

        try:
            product = Product.objects.get(article_uuid=product_id)
        except Product.DoesNotExist:
            return Response({'message': 'Продукт не найден'}, status=status.HTTP_404_NOT_FOUND)

        user = self.request.user

        try:
            cart_item = Cart.objects.get(user_id=user, product_list__product_id=product)
        except Cart.DoesNotExist:
            product_list = ProductList.objects.create(product_id=product, quantity=quantity)
            cart_item = Cart.objects.create(user_id=user, product_list=product_list)
        else:
            cart_item.product_list.quantity += quantity
            cart_item.product_list.save()

        serializer = CartSerializer(cart_item)

        return Response(serializer.data, status=status.HTTP_201_CREATED if not cart_item else status.HTTP_200_OK)


class CartEditProducts(generics.UpdateAPIView):
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({'message': 'Продукт не найден'}, status=status.HTTP_404_NOT_FOUND)

        user = self.request.user

        try:
            cart_item = Cart.objects.get(user_id=user, product_list__product_id=product)
        except Cart.DoesNotExist:
            return Response({'message': 'Продукт не найден в корзине'}, status=status.HTTP_404_NOT_FOUND)

        cart_item.product_list.quantity = quantity
        cart_item.product_list.save()

        serializer = CartSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CartDeleteProduct(generics.DestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')

        user = self.request.user

        try:
            cart_item = Cart.objects.get(user_id=user, product_list__product_id=product_id)
        except Cart.DoesNotExist:
            return Response({'message': 'Продукт не найден в корзине'}, status=status.HTTP_404_NOT_FOUND)

        cart_item.delete()

        return Response({'message': 'Продукт успешно удален из корзины'}, status=status.HTTP_204_NO_CONTENT)

