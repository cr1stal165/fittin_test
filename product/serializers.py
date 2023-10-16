from rest_framework import serializers

from category.models import Category
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False)

