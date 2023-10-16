from django.db import models

from product.models import Product


# Create your models here.


class ProductList(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


