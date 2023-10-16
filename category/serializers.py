from rest_framework import serializers

from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'children')

    def get_children(self, obj):
        children = Category.objects.filter(parent=obj)
        serializer = CategorySerializer(children, many=True)
        return serializer.data
