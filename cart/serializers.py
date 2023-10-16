from rest_framework import serializers

from product.models import Product
from product.serializers import ProductSerializer
from .models import Cart


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'
        extra_kwargs = {
            'user_id': {'required': False},
        }


