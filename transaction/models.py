from django.db import models

from order.models import Order
from product_list.models import ProductList


# Create your models here.

class Transaction(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_list_id = models.ForeignKey(ProductList, on_delete=models.CASCADE)
