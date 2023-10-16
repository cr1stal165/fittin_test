import datetime

from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cart.models import Cart
from order.models import Order
from order.serializers import OrderSerializer
from transaction.models import Transaction


# Create your views here.


class OrderCreate(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        order_date = datetime.datetime.today().date()
        date_of_receiving = request.data.get('date_of_receiving')
        address = request.data.get('address')
        user = self.request.user

        order = Order.objects.create(date_of_receiving=date_of_receiving, address=address, user=user, order_date=order_date)

        cart = Cart.objects.all()
        for prod_lst in cart:
            Transaction.objects.create(
                order_id=order,
                product_list_id=prod_lst.product_list
            ).save()
        cart.delete()
        serializer = OrderSerializer(order)
        return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)


